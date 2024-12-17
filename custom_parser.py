from globals import *
from validator import is_valid_factorial, dev_by_zero, pow_vali,incorrect_pow,tilda_checker
from minus_handling import *
from customExceptions import *


def string_to_lst_conv(inpt):
    return list(inpt)

def white_spaces_remover(inpt):
    inpt_lst = [letter for letter in string_to_lst_conv(inpt) if not letter.isspace()]
    return list(''.join(inpt_lst))

def infix_to_postfix(expression):
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
            output.append(number)  # Append the full number to the output

        # Handle sign minus ` (highest priority)
        elif char == '`':
            while stack and operator_priority.get(stack[-1], 0) >= operator_priority[char]:
                output.append(stack.pop())
            stack.append(char)

        # Handle unary minus _
        elif char == '_':
            stack.append('_')

        # Handle other operators
        elif char in supported_operators:
            while stack and stack[-1] != '(' and operator_priority.get(stack[-1], 0) >= operator_priority[char]:
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

    return output


def calc(postfix_expression):
    stack = []

    for token in postfix_expression:
        # Handle numbers (integers and floats)
        if token.isdigit() or '.' in token:
            stack.append(float(token) if '.' in token else int(token))

        # Handle unary minus '_'
        elif token == '_':
            if not stack:
                raise MissingOperandsException("Missing operand for unary minus '_'.")
            num = stack.pop()
            stack.append(-num)

        # Handle sign minus '`'
        elif token == '`':
            if not stack:
                raise MissingOperandsException("Missing operand for sign minus '`'.")
            num = stack.pop()
            stack.append(-num)

        # Handle supported operators
        elif token in operator_functions:
            # Unary operators
            if operator_operands[token] == 1:
                if not stack:
                    raise MissingOperandsException(f"Missing operand for unary operator '{token}'.")
                num = stack.pop()
                if token == '!':
                    # Ensure num is a non-negative integer
                    if not is_valid_factorial(num):
                        raise InvalidFactorialException(
                            "Factorial operator '!' cannot follow a number smaller than 0 or between 0 and 1.")
                    stack.append(operator_functions[token](num))
                else:
                    stack.append(operator_functions[token](num))

            # Binary operators
            elif operator_operands[token] == 2:
                if len(stack) < 2:
                    raise MissingOperandsException(f"Missing operands for binary operator '{token}'.")
                second = stack.pop()
                first = stack.pop()

                # Check for division by zero
                if token == '/' and not dev_by_zero(second):
                    raise ZeroDivisionError("Division by zero is not allowed.")

                # Check for invalid power operations
                if token == '^' and not pow_vali(first, second):
                    raise PowerException("Zero to the power of zero is undefined.")
                if token == '^' and not incorrect_pow(first, second):
                    raise PowerException(
                        f"Invalid operation: cannot compute an even root of a negative number {first} in a power of {second}.")

                stack.append(operator_functions[token](first, second))

        # Unsupported operator
        else:
            raise ValueError(f"Unsupported operator: {token}")

    # Final validation: There should be exactly one value left on the stack
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression. Too many operands left on the stack.")

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
