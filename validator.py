from customExceptions import *
from globals import *
from minus_handling import *
def all_white_chars(inpt):
    if not inpt.strip():
        raise AllWhiteSpaceException("Input contains only whitespace.")
    return True

def dot_checker(inpt):
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
            '''if indx >= 2 and inpt[indx - 2] == '-':
                raise InvalidFactorialException("Factorial operator '!' cannot follow a negative sign '-'.")'''
        indx += 1
    return True



def tilda_checker(inpt):
    # Tilde cannot be the last character
    if inpt[len(inpt) - 1] == '~':
        raise InvalidTildeException("Tilde '~' cannot be the last character in the expression.")

    for indx in range(len(inpt)):
        if inpt[indx] == '~':
            if indx < len(inpt) - 1:
                next_char = inpt[indx + 1]
                # Tilde must be followed directly by a digit or a valid unary minus (-)
                if not (next_char.isdigit() or (next_char == '-' and indx + 2 < len(inpt) and inpt[indx + 2].isdigit())):
                    raise InvalidTildeException("Invalid placement of tilde '~'. It must be followed by a digit or a unary minus '-'.")
    return True


def repeating_signs(inpt):
    length = len(inpt)
    for i in range(length - 1):
        if inpt[i] in operators_no_repeat and inpt[i]==inpt[i + 1] :
            raise RepeatingSigneException(f"Repeating signs detected: '{inpt[i]}' followed by '{inpt[i + 1]}'")

    return True


def check_not_missing_operand(inpt):
    i = 0
    while i < len(inpt):
        char = inpt[i]

        # Check if the current character is a binary operator
        if char in operator_operands and operator_operands[char] == 2:
                # Check if the operator is unary minus, if it is returns true
                if char == '-' and not is_binary(i,inpt) and i < len(inpt) - 1:
                    return True
                # Check if there's a missing operand before the operator
                if i == 0 or (not inpt[i - 1].isdigit() and inpt[i - 1] != ')' and inpt[i - 1] != '!'):
                    raise MissingOperandsException(f"Missing operand before operator '{char}' at position {i}")
                # Check if there's a missing operand after the operator
                if i == len(inpt) - 1 or (
                        not inpt[i + 1].isdigit() and inpt[i + 1] != '(' and inpt[i + 1] != '~' and inpt[i + 1] != '-'):
                    raise MissingOperandsException(f"Missing operand after operator '{char}' at position {i}")
        i += 1
    return True


'''הפונקציות שמתחת יקראו בזמן החישוב עצמו ולא במהלך הבדיקה המקדימה'''

def pow_vali(base,exponent):
    if base==0 and exponent==0:
        return False
    return True

def is_valid_factorial(num):
    if num<0 or 0<num<1: return False
    return True

def dev_by_zero(denominator ):
    if not denominator==0:
        return False
    return True

def main():
    '''
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