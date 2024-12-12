from validator import *
from custom_parser import*
from operations import *
from globals import *

def calculate(inpt):
    while True:
        try:
            # Remove whitespace first
            all_white_chars(inpt)
            inpt = white_spaces_remover(inpt)

            # Perform all necessary checks
            unexpected_letters(inpt)
            dot_checker(inpt)
            tilda_checker(inpt)
            repeating_signs(inpt)
            brackets_checker(inpt)
            factorial_checker(inpt)


            break  # If all checks pass, break the loop
        except (AllWhiteSpaceException, InvalidDotPlacementException, UnexpectedCharacterException,RepeatingSigneException,
                MismatchedBracketsException, InvalidFactorialException, InvalidTildeException) as e:
            print(f"Error: {e}")
            inpt = input("Please enter a valid expression: ")

    print("Input is valid:", inpt)
    print("Starting calculation")
    print(infix_to_postfix(inpt))
    print("res: ", calc(infix_to_postfix(inpt)))


def main():
    user_input = input("Enter something: ")
    calculate(user_input)

if __name__ == "__main__":
    main()