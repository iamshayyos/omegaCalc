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
    print(all_white_chars(input("enter smth")))

if __name__ == "__main__":
    main()

#2+4    (5/3+1)^2