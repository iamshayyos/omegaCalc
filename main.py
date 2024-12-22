"""
main.py

This module provides the main entry point for the calculator program.
It takes user input, processes expressions using the `calculate` function from `manager.py`,
and handles exceptions to provide appropriate feedback.
"""

from manager import calculate

def main():
    """
    The main function that runs the calculator application in a loop until the user exits.

    It prompts the user for an equation, calculates the result, and handles exceptions gracefully.
    """
    print(
        "Welcome to the calculator program!\n"
        "Supported operations:\n"
        "+, -, *, /, power (x^y), average (x@y), max (x$y), min (x&y), modulo (x%y),\n"
        "negative (~x), factorial (x!), sum of digits (xyz# -> x+y+z).\n"
        "Type 'end' to exit the calculator.\n"
    )

    while True:
        try:
            inpt = input("Enter an equation (or 'end' to quit): ")
            if inpt.lower() == "end":
                print("Goodbye!")
                break

            # Calculate the result using the manager module
            result = calculate(inpt)
            print(f"Result: {result}")

        except EOFError:
            print("Input ended unexpectedly. Exiting.")
            break
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
