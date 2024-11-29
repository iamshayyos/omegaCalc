from parser import white_spaces_remover
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
    i=0
    while i<len(inpt):
        if inpt[i]==".":
            if i + 1 < len(inpt) and inpt[i + 1] != "." and inpt[i - 1].isdigit():
                i += 1
            else: return False
        elif inpt[i].isdigit():
            i+=1
        elif inpt[i] in operator_operands:
            i+=1
        else:
            return False
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