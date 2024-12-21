"""
validator.py

This module contains functions to validate mathematical expressions before they are processed or evaluated.
It includes checks for:
- Whitespace-only inputs
- Dot placements
- Unexpected characters
- Unmatched parentheses
- Invalid factorial usage
- Invalid power usage
- Repeating signs
- Incorrect tilde placements
- Missing operands
- Division by zero
"""

from customExceptions import *
from globals import *
from minus_handling import *
def all_white_chars(inpt):
    """
        Checks if the input contains only whitespace.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if the input is valid.

        Raises:
            AllWhiteSpaceException: If the input contains only whitespace.
        """
    if not inpt.strip():
        raise AllWhiteSpaceException("Input contains only whitespace.")
    return True

def dot_checker(inpt):
    """
        Checks for invalid dot placements in numbers (multiple dots).

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if the dot placement is valid.

        Raises:
            InvalidDotPlacementException: If a number contains multiple dots.
        """
    i = 0
    current_number = ""
    has_dot = False

    while i < len(inpt):
        char = inpt[i]

        if char.isdigit() or char == ".":
            current_number += char
            if char == ".":
                if has_dot:
                    raise InvalidDotPlacementException("Invalid dot placement: multiple dots in a single number.")
                has_dot = True
        else:
            # When we encounter a non-digit, non-dot character, reset the number and dot flag
            current_number = ""
            has_dot = False

        i += 1
    return True


def unexpected_letters(inpt):
    """
       Checks for unexpected characters in the input.

       Args:
           inpt (str): The input string to check.

       Returns:
           bool: True if no unexpected characters are found.

       Raises:
           UnexpectedCharacterException: If an unexpected character is found.
       """
    for char in inpt:
        if not char.isdigit() and char not in SUPPORTED_OPERATORS and char != '(' and char != ')' and char != '.':
            raise UnexpectedCharacterException(f"Unexpected character found: '{char}'")
    return True


def brackets_checker(inpt):
    """
        Checks for unmatched or improperly placed parentheses.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if parentheses are properly matched and placed.

        Raises:
            BracketsException: If mismatched or empty parentheses are found.
        """
    brackets_stack = []  # Stack to keep track of the positions of opening brackets '('

    # Iterate through each character in the input string
    for i, char in enumerate(inpt):
        # If the character is an opening bracket '('
        if char == '(':
            # Check for multiplication before '('
            if i > 0 and (inpt[i - 1].isdigit() or inpt[i - 1] == ')'):
                raise BracketsException("Multiplication is not allowed before '('.")

            brackets_stack.append(i)

        # If the character is a closing bracket ')'
        if char == ')':
            # Check for multiplication after ')'
            if i + 1 < len(inpt) and inpt[i + 1].isdigit():
                raise BracketsException("Multiplication is not allowed after ')'.")

            # If the stack is empty, there's no matching opening bracket
            if len(brackets_stack) == 0:
                raise BracketsException("Mismatched closing bracket ')'.")

            # Pop the position of the last unmatched opening bracket '('
            opening_index = brackets_stack.pop()

            # Check if the parentheses are empty (i.e., no content between '(' and ')')
            if i - opening_index == 1:
                raise BracketsException("Empty parentheses '()' are not allowed.")

    # After iterating through the input, if the stack is not empty, there are unmatched '('
    if len(brackets_stack) != 0:
        raise BracketsException("Mismatched opening bracket '('.")

    return True  # The input is valid if no exceptions were raised


def factorial_checker(inpt):
    """
        Checks for valid usage of the factorial operator '!'.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if factorial usage is valid.

        Raises:
            InvalidFactorialException: If factorial is misused.
        """
    indx = 0
    while indx < len(inpt):
        if inpt[indx] == '!':
            if indx == 0:
                raise InvalidFactorialException("Expression cannot start with a factorial operator '!'.")
            if not inpt[indx - 1].isdigit() and inpt[indx - 1] != ')' and inpt[indx - 1] != '!' and inpt[indx - 1] != '#':
                raise InvalidFactorialException("Factorial operator '!' must follow a digit or a closing parenthesis ')'.")
        indx += 1
    return True


def hash_vali(inpt):
    """
        Checks for invalid hashtag '#' placement.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if hashtag placement is valid.

        Raises:
            HashtagException: If '#' is at the start or followed by a digit.
        """

    # Check if '#' is the first character in the input
    if inpt[0] == '#':
        raise HashtagException("Hashtag '#' cannot start the expression.")

    for i in range(len(inpt)):
        if inpt[i] == '#':
            # Check if # is followed by a digit
            if i + 1 < len(inpt) and inpt[i + 1].isdigit():
                raise HashtagException("Hashtag '#' cannot be followed by a digit.")
            if not inpt[i - 1].isdigit() and inpt[i - 1] != ')' and inpt[i - 1] != '!' and inpt[i - 1] != '#':
                raise InvalidFactorialException("Hashtag operator '#' must follow a digit or a closing parenthesis ')'.")


def tilda_checker(inpt):
    """
        Checks for invalid tilde '~' placement.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if tilde placement is valid.

        Raises:
            InvalidTildeException: If '~' is at the end or followed by invalid characters.
        """
    # Tilde cannot be the last character
    if inpt[-1] == '~':
        raise InvalidTildeException("Tilde '~' cannot be the last character in the expression.")

    for indx in range(len(inpt)):
        if inpt[indx] == '~':
            if indx >= len(inpt) - 1:
                raise InvalidTildeException("Tilde '~' must be followed by a digit, unary minus '-', sign minus '`', or an opening parenthesis '('.")

            next_char = inpt[indx + 1]
            # Check if followed by a digit, unary minus '_', sign minus '`', or an opening parenthesis '('
            if not (next_char.isdigit() or next_char in ('_', '`', '(')):
                raise InvalidTildeException("Invalid placement of tilde '~'. It must be followed by a digit, unary minus '-', sign minus '`', or an opening parenthesis '('.")

    return True




def repeating_signs(inpt):
    """
        Checks for consecutive repeating signs that are not allowed.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if no repeating signs are found.

        Raises:
            RepeatingSigneException: If consecutive repeating signs are detected.
        """
    length = len(inpt)
    for i in range(length - 1):
        if inpt[i] in OPERATORS_NO_REPEAT and inpt[i]==inpt[i + 1] :
            raise RepeatingSigneException(f"Repeating signs detected: {inpt[i]} followed by {inpt[i + 1]}")

    return True

def is_valid_tilde(inpt):
    """
        Checks if the tilde '~' is placed correctly in the input string.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if tilde placement is valid.

        Raises:
            InvalidTildeException: If the tilde '~' is placed incorrectly.
        """
    for indx in range(len(inpt)):
        if inpt[indx] == '~':
            if indx==0:
                continue
            # Check if the character before ~ is not a binary operator
            if inpt[indx - 1] not in BINARY_OPERATORS and inpt[indx - 1]!='(' and not (inpt[indx - 1]=='-' and is_binary(indx-1,inpt)):
                raise InvalidTildeException("Invalid placement of tilde '~'. It must follow a binary operator.")


def check_not_missing_operand(inpt):
    """
        Checks if there are missing operands around binary operators.

        Args:
            inpt (str): The input string to check.

        Returns:
            bool: True if no operands are missing.

        Raises:
            MissingOperandsException: If an operator is missing operands before or after it.
        """
    i = 0
    while i < len(inpt):
        char = inpt[i]

        # Check if the current character is a binary operator
        if char in OPERATOR_OPERANDS and OPERATOR_OPERANDS[char] == 2:
                # Check if the operator is unary minus, if it is returns true
                if char == '-' and not is_binary(i,inpt) and i < len(inpt) - 1:
                    return True
                # Check if there's a missing operand before the operator
                if i == 0 or (not inpt[i - 1].isdigit() and inpt[i - 1] != ')' and inpt[i - 1] != '!' and inpt[i - 1] != '#'):
                    raise MissingOperandsException(f"Missing operand before operator {char} at position {i}")
                # Check if there's a missing operand after the operator
                if i == len(inpt) - 1 or (not inpt[i + 1].isdigit() and inpt[i + 1] != '(' and inpt[i + 1] != '~' and inpt[i + 1] != '-'):
                    raise MissingOperandsException(f"Missing operand after operator {char} at position {i}")
        i += 1
    return True




def pow_vali(base,exponent):
    """
       Validates if the power operation is valid (0^0 is invalid).

       Args:
           base (float): The base of the power operation.
           exponent (float): The exponent of the power operation.

       Returns:
           bool: False if the power operation is invalid (0^0), otherwise True.
       """
    return False if base==0 and exponent==0 else True

def incorrect_pow(base,exponent):
    """
        Checks for invalid power operations with negative bases and fractional exponents.

        Args:
            base (float): The base of the power operation.
            exponent (float): The exponent of the power operation.

        Returns:
            bool: False if the power operation is invalid, otherwise True.
        """
    return False if (base < 0 < exponent < 1 or (base<0 and -1<exponent<0) ) else True

def is_valid_factorial(num):
    """
        Checks if a number is valid for a factorial operation.

        Args:
            num (float): The number to check.

        Returns:
            int:
                - 0 if the number is a non-negative integer (valid case).
                - 1 if the number is negative or between 0 and 1.
                - 2 if the number is not an integer.
        """
    num=float(num)
    if num < 0 or (0 < num < 1):
        return 1  # Indicates the number is negative or between 0 and 1
    if not (isinstance(num, int) or (isinstance(num, float) and num.is_integer())):
        return 2  # Indicates the number is not an integer
    return 0  # Valid case: non-negative integer


def dev_by_zero(denominator ):
    """
        Checks if the denominator is zero to prevent division by zero.

        Args:
            denominator (float): The denominator to check.

        Returns:
            bool: False if the denominator is zero, otherwise True.
        """
    return denominator!=0

def main():
    ''' inpt=input("enter smth: ")
    #ex="-5+-3-4*(-2)-2"
    ex = "2-----2"
    print(is_binary_minus(ex,2))
    inpt=input("enter smth: ")
    while inpt!='.':
        print(is_binary_minus(ex,int(inpt)))
        inpt = input("enter smth: ")
'''

if __name__ == "__main__":
    main()

#2+4    (5/3+1)^2'''