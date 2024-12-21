"""
custom_parser.py

This module contains functions for parsing mathematical expressions, converting infix expressions to postfix,
and evaluating postfix expressions. It handles various operators, including unary minus, sign minus, factorial,
and custom operations like hashtag and power.
"""


from globals import *
from validator import is_valid_factorial, dev_by_zero, pow_vali,incorrect_pow,tilda_checker
from minus_handling import *
from customExceptions import *


def string_to_lst_conv(inpt):
    """
        Converts a string into a list of its characters.

        Args:
            inpt (str): The input string.

        Returns:
            list: A list of characters from the input string.
        """
    return list(inpt)

def white_spaces_remover(inpt):
    """
        Removes all whitespace characters from the input string.

        Args:
            inpt (str): The input string containing whitespace.

        Returns:
            list: A list of characters with whitespace removed.
        """
    inpt_lst = [letter for letter in string_to_lst_conv(inpt) if not letter.isspace()]
    return list(''.join(inpt_lst))

def infix_to_postfix(expression):
    """
        Converts an infix expression to a postfix expression using the Shunting Yard algorithm.

        Args:
            expression (str): The infix mathematical expression.

        Returns:
            list: The postfix expression as a list of tokens.
        """
    output = []  # Postfix expression
    stack = []  # Operator stack
    i = 0

    expression = minus_destroyer(expression)
    tilda_checker(expression)
    while i < len(expression):
        char = expression[i]

        # Check for numbers (multi-digit and with potential decimals)
        if char.isdigit():
            number = char
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                i += 1
                number += expression[i]
            output.append(str(number))  # Ensure the full number is appended as a string

        # Handle sign minus ` (highest priority)
        elif char == '`':
            while stack and OPERATOR_PRIORITY.get(stack[-1], 0) >= OPERATOR_PRIORITY[char]:
                output.append(stack.pop())
            stack.append(char)

        # Handle unary minus _
        elif char == '_':
            stack.append('_')

        # Handle other operators
        elif char in SUPPORTED_OPERATORS:
            while stack and stack[-1] != '(' and OPERATOR_PRIORITY.get(stack[-1], 0) >= OPERATOR_PRIORITY[char]:
                output.append(stack.pop())
            stack.append(char)

        # Handle opening parenthesis
        elif char == '(':
            stack.append(char)

        # Handle closing parenthesis
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from the stack

        i += 1

    # Pop any remaining operators from the stack to the output
    while stack:
        output.append(stack.pop())

    # Ensure all numbers in the output are strings
    output = [str(token) for token in output]

    return output


def calc(postfix_expression):
    """
        Evaluates a postfix expression and returns the result.

        Args:
            postfix_expression (list): The postfix expression as a list of tokens.

        Returns:
            float or int: The result of the evaluated postfix expression.

        Raises:
            MissingOperandsException: If an operator is missing operands.
            ZeroDivisionError: If division by zero is attempted.
            PowerException: If a power operation is invalid.
            LargeNumberException: If the result is too large to compute.
            HashtagException: If the hashtag operation is applied to a negative number.
        """

    stack = []

    for token in postfix_expression:
        # Handle numbers (integers and floats)
        if token.isdigit() or '.' in token:
            stack.append(str(token) if '.' in token else str(token))

        # Handle unary minus '_'
        elif token == '_':
            if not stack:
                raise MissingOperandsException("Missing operand for unary minus '_'.")
            num = stack.pop()
            stack.append(str(-int(num)))

        # Handle sign minus '`'
        elif token == '`':
            if not stack:
                raise MissingOperandsException("Missing operand for sign minus '`'.")
            num = stack.pop()
            stack.append(str(-float(num)))

        # Handle supported operators
        elif token in OPERATOR_FUNCTIONS:
            # Unary operators
            if OPERATOR_OPERANDS[token] == 1:
                if not stack:
                    raise MissingOperandsException(f"Missing operand for unary operator '{token}'.")
                num = stack.pop()
                if token == '!':
                    # Ensure num is a non-negative integer
                    if is_valid_factorial(num) == 1:
                        raise InvalidFactorialException("Factorial operator '!' cannot follow a number smaller than 0 or between 0 and 1.")
                    if is_valid_factorial(num) == 2:
                        raise InvalidFactorialException("Factorial operator '!' cannot follow a non-integer number.")
                    if float(num) > 170:
                        raise LargeNumberException("The largest number that this calculator can handle for factorial is 170.")
                    stack.append(OPERATOR_FUNCTIONS[token](num))

                elif token == '#':
                    # Convert num to float or int before validating
                    num = float(num) if '.' in num else int(num)

                    # Check if the number is negative and raise an exception
                    if num < 0:
                        raise HashtagException("Cannot perform hashtag '#' operation on a negative number.")

                    # Perform the hashtag operation
                    stack.append(hashtag(num))

                else:
                    stack.append(OPERATOR_FUNCTIONS[token](num))

            # Binary operators
            elif OPERATOR_OPERANDS[token] == 2:
                if len(stack) < 2:
                    raise MissingOperandsException(f"Missing operands for binary operator '{token}'.")
                second = float(stack.pop())
                first = float(stack.pop())

                # Check for division by zero
                if (token == '/' or token=='%') and not dev_by_zero(second):
                    raise ZeroDivisionError("Division by zero is not allowed.")

                if token == '^':
                    # Check for invalid power operations
                    if not pow_vali(first, second):
                        raise PowerException("Zero to the power of zero is undefined.")
                    if not incorrect_pow(first, second):
                        raise PowerException(f"Invalid operation: cannot compute an even root of a negative number {first} in a power of {second}.")

                    try:
                        # Check for large results (overflow)
                        if second > 308:
                            raise LargeNumberException("Result too large to compute.")
                        if (first ** second) > 1.7976931348623157e+308:
                            raise LargeNumberException("Result too large to compute.")
                        # Check for small results (underflow)
                        if 0 < (first ** second) < 5e-324:
                            raise SmallNumberException("Result too small to represent (underflow).")
                    except OverflowError:
                        raise LargeNumberException("Result too large to compute.")

                stack.append(OPERATOR_FUNCTIONS[token](first, second))

        # Unsupported operator
        else:
            raise ValueError(f"Unsupported operator: {token}")

    # Final validation: There should be exactly one value left on the stack
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression. Too many operands left on the stack.")

    # Check for large results
    if float(stack[0]) >= 1.8e308:
        raise LargeNumberException("Result too large to compute.")

    return stack[0]



def main():
    """"
    st = input("Enter something: ")
    print("Converted to list:", string_to_lst_conv(st))
    print("Without whitespaces:", white_spaces_remover(st))"""
    expression = ["3", "+", "5", "*", "(", "2", "-", "4", ")"]
    x=input("Enter something")

    while x!='.':
        postfix = infix_to_postfix(x)
        print("Postfix:", postfix)
        print("res: ",calc(postfix))
        x = input("Enter something")

if __name__ == "__main__":
    main()
