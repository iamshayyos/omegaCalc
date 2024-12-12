from contextlib import nullcontext

from customExceptions import *

operator_priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    "%": 4,
    "@": 5,
    "$": 5,
    "&": 5,
    "~": 6,
    "!": 6
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

def all_white_chars(inpt):
    if not inpt.strip():
        raise AllWhiteSpaceException("Input contains only whitespace.")
    return True

def dot_checker(inpt):
    i = 0
    while i < len(inpt):
        if inpt[i] == ".":
            # A dot must be surrounded by digits to be valid
            if i == 0 or i == len(inpt) - 1 or not (inpt[i - 1].isdigit() and inpt[i + 1].isdigit()) or ((i + 2) < len(inpt) and inpt[i + 2] == "."):
                raise InvalidDotPlacementException("Invalid dot placement detected.")
        elif inpt[i].isdigit() or inpt[i] in "()":
            # Digits and parentheses are valid
            pass
        elif inpt[i] in operator_operands:
            # Valid operators are allowed
            pass
        else:
            # If the character is neither a dot, digit, operator, nor parenthesis, it's invalid
            raise InvalidDotPlacementException(f"Unexpected character '{inpt[i]}' found in input.")
        i += 1
    return True



def unexpected_letters(inpt):
    for char in inpt:
        if not char.isdigit() and char not in operator_priority and char != '(' and char != ')' and char != '.':
            raise UnexpectedCharacterException(f"Unexpected character found: '{char}'")
    return True


def brackets_checker(inpt):
    brackets_stack = []
    for char in inpt:
        if char == '(':
            brackets_stack.append('(')
        if char == ')':
            if len(brackets_stack) == 0:
                raise MismatchedBracketsException("Mismatched closing bracket ')'.")
            brackets_stack.pop()

    if len(brackets_stack) != 0:
        raise MismatchedBracketsException("Mismatched opening bracket '('.")
    return True


def factorial_checker(inpt):
    indx = 0
    while indx < len(inpt):
        if inpt[indx] == '!':
            if indx == 0:
                raise InvalidFactorialException("Expression cannot start with a factorial operator '!'.")
            if not inpt[indx - 1].isdigit() and inpt[indx - 1] != ')':
                raise InvalidFactorialException("Factorial operator '!' must follow a digit or a closing parenthesis ')'.")
            if indx >= 2 and inpt[indx - 2] == '-':
                raise InvalidFactorialException("Factorial operator '!' cannot follow a negative sign '-'.")
        indx += 1
    return True



def is_binary_minus(expression, index):
    valid_for_unary = {"(", "+", "-", "/", "*"}  # Characters that allow a unary minus

    # Validate index is within range
    if index < 0 or index >= len(expression):
        return False

    # Ensure the character at the index is a minus sign
    if expression[index] != "-":
        return False

    # Check if it's the first character
    if index == 0:
        return False  # A minus at the start is unary

    # Check the character before the minus
    prev_char = expression[index - 1]

    # If the character before is valid for unary, it's unary
    return not (prev_char in valid_for_unary)

def tilda_checker(inpt):#

    # Tilde cannot be the last character
    if inpt[len(inpt)-1]=='~':
        raise InvalidTildeException

    for indx in range(len(inpt)):
        if inpt[indx] == '~':
            if indx<len(inpt):
                next_char = inpt[indx + 1]
                # Tilde must be followed directly by a digit or a valid unary minus (-)
                if not (next_char.isdigit() or (next_char == '-' and  inpt[indx+2].isdigit())):
                    raise InvalidTildeException
    return True


def pow_vali(base,exponent):
    if base==0 and exponent==0:
        raise ZeroToThePowerZeroException
    return True


def dev_by_zero(denominator ):
    if not denominator==0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return True


'''def main():
    #ex="-5+-3-4*(-2)-2"
    ex = "~-3"
    #print(is_binary_minus(ex,4))
    inpt=input("enter smth: ")
    while inpt!='.':
        print(pow_vali(inpt))
        inpt = input("enter smth: ")


if __name__ == "__main__":
    main()

#2+4    (5/3+1)^2'''