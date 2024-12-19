from manager import calculate
def main():
    try:
        inpt = input('Enter an equation using the following operators:\n'
                     '+ - * / \n'
                     'In addition, you can use power x^y, avg x@y, max x$y, min x&y, modulo x%y, '
                     'negative value ~x, factorial x!, sum of the number digits xyz# -> x+y+z.\n'
                     'Type "end" to exit the calculator.\n\nEnter an equation: ')
        while inpt != "end":
            calculate(inpt)
            inpt = input("Enter new equation (or type 'end' to exit): ")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")
    print("Calculator exited. Goodbye!")
if __name__ == "__main__":
    main()