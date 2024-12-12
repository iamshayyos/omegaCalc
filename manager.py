from validator import *
from custom_parser import*
from operations import *
operator_priority = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "^": power,
    "%": modulo,
    "@": avg,
    "$":max_value,
    "&": min_value,
    "~": negative,
    "!": factorial
}
operator_operands = {
    "+": 2,
    "-": 2,
    "*": 2,
    "/": 2,
    "^": 2,
    "%": 2,
    "@": 2,
    "$": 2,
    "&": 2,
    "~": 1,
    "!": 1
}


def calculate(inpt):
    while True:
        try:
            # Remove whitespace first
            all_white_chars(inpt)
            inpt = white_spaces_remover(inpt)

            # Perform all necessary checks
            unexpected_letters(inpt)
            dot_checker(inpt)
            brackets_checker(inpt)
            factorial_checker(inpt)
            tilda_checker(inpt)

            break  # If all checks pass, break the loop
        except (AllWhiteSpaceException, InvalidDotPlacementException, UnexpectedCharacterException,
                MismatchedBracketsException, InvalidFactorialException, InvalidTildeException) as e:
            print(f"Error: {e}")
            inpt = input("Please enter a valid expression: ")

    print("Input is valid:", inpt)


def main():
    user_input = input("Enter something: ")
    calculate(user_input)

if __name__ == "__main__":
    main()