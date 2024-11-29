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
            # Reset dot validity when encountering an operator
            pass
        else:
            # If the character is neither a dot, digit, nor operator, it's invalid
            return False
        i += 1
    return True

def unexpected_letters(inpt):
    pass
def fun1(inpt):
    inpt=white_spaces_remover(inpt)
    print(dot_checker(inpt))

def main():
    fun1(input("enter smth"))

if __name__ == "__main__":
    main()

#2+4    (5/3+1)^2