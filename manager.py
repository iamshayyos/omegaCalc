from validator import *
from custom_parser import *
from globals import *

def calculate(inpt):
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
