"""
manager.py

This module contains the `calculate` function, which orchestrates the validation,
parsing, and evaluation of mathematical expressions. It raises appropriate exceptions
if the input is invalid.
"""


from validator import *
from custom_parser import *
from globals import *

def calculate(inpt):
    """
        Validates, parses, and calculates the result of a mathematical expression.

        Args:
            inpt (str): The mathematical expression in string format.

        Returns:
            float or int: The result of the evaluated expression.

        Raises:
            AllWhiteSpaceException: If the input contains only whitespace.
            InvalidDotPlacementException: If a number contains multiple dots.
            UnexpectedCharacterException: If the input contains invalid characters.
            RepeatingSigneException: If the input has consecutive invalid operators.
            BracketsException: If there are mismatched parentheses.
            InvalidFactorialException: If a factorial operation is applied incorrectly.
            MissingOperandsException: If an operator is missing operands.
            HashtagException: If the hashtag operation is used incorrectly.
            InvalidTildeException: If the tilde operation is used incorrectly.
            PowerException: If a power operation is invalid.
            ZeroDivisionError: If a division by zero occurs.
            LargeNumberException: If the result or input is too large to handle.
        """


    while True:
        try:

            # Remove whitespace first
            inpt=inpt.strip()
            all_white_chars(inpt)
            inpt = white_spaces_remover(inpt)

            # Perform all necessary checks
            unexpected_letters(inpt)
            dot_checker(inpt)
            is_valid_tilde(inpt)
            hash_vali(inpt)
            repeating_signs(inpt)
            brackets_checker(inpt)
            check_not_missing_operand(inpt)
            factorial_checker(inpt)

            # If all checks pass, proceed to calculate
            postfix = infix_to_postfix(inpt)
            result = calc(postfix)
            return result  # Return the calculation result

        except (AllWhiteSpaceException, InvalidDotPlacementException, UnexpectedCharacterException,
                RepeatingSigneException, BracketsException, InvalidFactorialException,
                MissingOperandsException, HashtagException, InvalidTildeException,
                PowerException, ZeroDivisionError, LargeNumberException) as e:
            raise e  # Return the exception
