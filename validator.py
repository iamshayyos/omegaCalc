from operator import indexOf

from custom_parser import white_spaces_remover

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
    return False if inpt.isspace() else True

def dot_checker(inpt):
    i = 0
    while i < len(inpt):
        if inpt[i] == ".":
            # A dot must be surrounded by digits to be valid
            if i == 0 or i == len(inpt) - 1 or not (inpt[i - 1].isdigit() and inpt[i + 1].isdigit()) or ((i+2)<len(inpt)and inpt[i+2]=="."):
                return False
        elif inpt[i].isdigit():
            # Move forward for digits
            pass
        elif inpt[i] in operator_operands:
            pass
        else:
            # If the character is neither a dot, digit, nor operator, it's invalid
            return False
        i += 1
    return True

def unexpected_letters(inpt):
    for char in inpt:
        if not char.isdigit() and char not in operator_priority and char!='(' and char!=')' and char != '.':
            return False
    return True

def brackets_checker(inpt):
    brackets_stack=[]
    for char in inpt:
        if char== '(':
            brackets_stack.append('(')
        if char==')':
            if len(brackets_stack)==0:
                return False
            brackets_stack.pop()
    return len(brackets_stack)==0

def tilda_checker(inpt):#
    indx=0
    if inpt[len(inpt)-1]=='~':
        return False
    while indx<len(inpt):
        if inpt[indx]!='~':
            indx+=1
        else:
            if not (indx+1<len(inpt) and (inpt[indx+1].isdigit()  or inpt[indx+1]=='-')):
                return False
            indx+=1
    return True

def factorial_checker(inpt):#לבדוק אם !!5 יעבוד ו!(!5)
    indx=0
    if inpt[indx]=='!':
        return False
    indx+=1
    while indx<len(inpt):
        if inpt[indx]=='!' and not inpt[indx-1].isdigit():
            return False
        indx+=1
    return True

def is_binary_minus(expression, index):
    valid_for_unary = {"(", "+", "-", "/", "*"}  # Characters that allow a unary minus

    # Validate index is within range
    if index < 0 or index >= len(expression):
        return None  # Invalid index

    # Ensure the character at the index is a minus sign
    if expression[index] != "-":
        return None  # Not a minus sign

    # Check if it's the first character
    if index == 0:
        return False  # A minus at the start is unary

    # Check the character before and after the minus
    prev_char = expression[index - 1]
    next_char = expression[index + 1] if index + 1 < len(expression) else ""

    # If the character before is valid for unary, it's unary
    if prev_char in valid_for_unary:
        return False  # Unary

    # If the character before is a digit or closing parenthesis, it's binary
    if prev_char.isdigit() or prev_char == ")":
        return True  # Binary

    # If the next character is valid for unary (number or opening parenthesis), it's unary
    if next_char.isdigit() or next_char == "(":
        return False  # Unary

    # Default case: assume unary
    return False

def minus_val(inpt):
    processed_expression = []
    n = len(inpt)
    i = 0

    while i < n:
        char = inpt[i]

        # Handle unary minus
        if char == '-' and (
                i == 0 or inpt[i - 1] in operator_operands
        ):
            processed_expression.append("~")  # Replace unary minus with distinct marker
        else:
            processed_expression.append(char)

        i += 1

    return ''.join(processed_expression)

def dev_by_zero(inpt):
    ...


def main():
    ex="5+-3-4*(-2)"
    print(is_binary_minus(ex,4))

if __name__ == "__main__":
    main()

#2+4    (5/3+1)^2