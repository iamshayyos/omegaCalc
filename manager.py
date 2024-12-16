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

            repeating_signs(inpt)
            brackets_checker(inpt)
            check_not_missing_operand(inpt)
            factorial_checker(inpt)

            break  # If all checks pass, break the loop
        except (AllWhiteSpaceException, InvalidDotPlacementException, UnexpectedCharacterException,
                RepeatingSigneException, MismatchedBracketsException, InvalidFactorialException,
                MissingOperandsException) as e:
            print(f"Error: {e}")
            inpt = input("Please enter a valid expression: ")

    '''
    print("Input is valid:", inpt)
    print("Starting calculation")'''

    while True:
        try:
            postfix = infix_to_postfix(inpt)  # Convert to postfix once
            #print("Postfix Expression:", postfix)
            result = calc(postfix)            # Calculate the result
            print("Result:", result)
            break
        except (PowerException, InvalidFactorialException, ZeroDivisionError,MissingOperandsException,InvalidTildeException) as e:
            print(f"Error: {e}")
            inpt = input("Please enter a valid expression: ")
            # Re-validate the new input
            while True:
                try:
                    all_white_chars(inpt)
                    inpt = white_spaces_remover(inpt)
                    unexpected_letters(inpt)
                    dot_checker(inpt)

                    repeating_signs(inpt)
                    brackets_checker(inpt)
                    check_not_missing_operand(inpt)
                    factorial_checker(inpt)
                    break
                except (AllWhiteSpaceException, InvalidDotPlacementException, UnexpectedCharacterException,
                        RepeatingSigneException, MismatchedBracketsException, InvalidFactorialException,
                        MissingOperandsException) as e:
                    print(f"Error: {e}")
                    inpt = input("Please enter a valid expression: ")



def main():
    user_input = input("Enter something: ")
    calculate(user_input)

if __name__ == "__main__":
    main()