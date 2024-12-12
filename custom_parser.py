from globals import *
from validator import is_binary_minus

def string_to_lst_conv(inpt):
    return list(inpt)

def white_spaces_remover(inpt):
    inpt_lst = [letter for letter in string_to_lst_conv(inpt) if not letter.isspace()]
    return list(''.join(inpt_lst))

def infix_to_postfix(expression):
    output = []  # Postfix expression
    stack = []  # Operator stack

    i = 0
    while i < len(expression):
        char = expression[i]
        # Check for numbers (multi-digit and with potential decimals)
        if char.isdigit():
            number = char
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                i += 1
                number += expression[i]
            output.append(number)  # Append the full number to the output
        # Handle minus (distinguish between unary and binary)
        elif char == '-':
            if is_binary_minus(expression, i):
                # Binary minus
                while stack and stack[-1] != '(' and operator_priority.get(stack[-1], 0) >= operator_priority[char]:
                    output.append(stack.pop())
                stack.append(char)
            else:
                # Unary minus
                stack.append('_')
        # Handle other operators
        elif char in supported_operators:
            while stack and stack[-1] != '(' and operator_priority.get(stack[-1], 0) >= operator_priority[char]:
                output.append(stack.pop())
            stack.append(char)
        # Handle opening parenthesis
        elif char == '(':
            stack.append(char)
        # Handle closing parenthesis
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from the stack
        i += 1
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
