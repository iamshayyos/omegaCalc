from manager import calculate
def main():
    inpt=input('Enter an equation use the following operators:\n + - * / \n In addition for those you can use power x^y, avg x@y, max x$y, min x&y, modulo x%y, negative value ~x, and factorial x!.\n write "end" to exit the calculator ')
    while inpt!="end":
        calculate(inpt)
        inpt=input("Enter new equation: ")
if __name__ == "__main__":
    main()