def string_to_lst_conv(inpt):
    return list(inpt)

def white_spaces_remover(inpt):
    inpt_lst = [letter for letter in string_to_lst_conv(inpt) if not letter.isspace()]
    return list(''.join(inpt_lst))

def infix_to_postfix(expression):
    precedence = {
        '+': 1,  # Addition
        '-': 1,  # Subtraction
        '*': 2,  # Multiplication
        '/': 2,  # Division
        '^': 3,  # Power
        '&': 5,  # Minimum
        '$': 5,  # Maximum
        '@': 5,  # AVG
        '%': 4,  # Modulo
        '!': 6,  # Factorial
        '~': 6   # Negation
    }
    supported_operators = {'+', '-', '*', '/', '^', '%', '&', '$', '@', '!', '~'}
    output = []  # Postfix expression
    stack = []  # Operator stack
    for char in expression:
        if char.isdigit():  # If the token is a number, add it to the output
            output.append(char)
        elif char in supported_operators:  # If the token is an operator
            while stack and precedence.get(stack[-1], 0) >= precedence[char]:
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':  # If the token is '(', push it onto the stack
            stack.append(char)
        elif char == ')':  # If the token is ')', pop until '(' is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from the stack

        # Pop any remaining operators from the stack to the output
    while stack:
        output.append(stack.pop())

    return output

def main():
    """"
    st = input("Enter something: ")
    print("Converted to list:", string_to_lst_conv(st))
    print("Without whitespaces:", white_spaces_remover(st))"""
    expression = ["3", "+", "5", "*", "(", "2", "-", "4", ")"]
    postfix = infix_to_postfix(input("Enter something"))
    print("Postfix:", postfix)

if __name__ == "__main__":
    main()
