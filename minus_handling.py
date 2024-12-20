"""
minus_handling.py

This module contains functions to handle expressions with minus signs. It simplifies consecutive minus
signs and determines if a minus sign is sign, unary or binary.
"""


def count_minus(pos, inpt):
    """
        Counts consecutive minus signs starting from a given position.

        Args:
            pos (int): The starting position in the input string.
            inpt (str): The input expression.

        Returns:
            int: The number of consecutive minus signs.
        """
    count = 0
    for i in range(pos, len(inpt)):
        if inpt[i] == '-':
            count += 1
        else:
            break
    return count

def is_unary_minus(pos, inpt):
    """
       Determines if a minus sign at a given position is unary.

       Args:
           pos (int): The position of the minus sign.
           inpt (str): The input expression.

       Returns:
           bool: True if the minus sign is unary, False otherwise.
       """

    # Check if the position is at the start of the string
    if pos == 0 and (inpt[pos + 1] in ('(', '-') or inpt[pos + 1].isdigit()):
        return True
    else:
        i = pos + 1
        j = pos - 1
        # Check characters after the current position
        while i < len(inpt) - 1 and not (inpt[i + 1] in ('(', '-') or inpt[i + 1].isdigit()):
            if inpt[i] != '-':
                return False
            i += 1
        # Check characters before the current position
        while j >= 0:
            if inpt[j] == '-':
                j -= 1
            elif inpt[j]=='(':
                return True
            return False

    return True

def is_binary(pos,inpt):
    """
       Determines if a minus sign at the given position is a binary minus.

       Args:
           pos (int): The position of the minus sign in the input string.
           inpt (str): The input expression.

       Returns:
           bool: True if the minus sign is a binary operator, False otherwise.
       """

    if pos==0: return False
    if len(inpt)>1 and not (inpt[pos-1].isdigit() or inpt[pos-1]=='!' or inpt[pos-1]=='#' or inpt[pos-1]==')'):
        return False
    return True

def minus_destroyer(inpt):
    """
        Simplifies consecutive minus signs in a mathematical expression.

        Args:
            inpt (str): The input expression containing minus signs.

        Returns:
            str: The expression with simplified minus signs, places different symbols of minus for each one.
        """

    i = 0
    inpt = list(inpt)  # Convert string to a mutable list

    while i < len(inpt):
        if inpt[i] == '-':
            count = count_minus(i, inpt)

            if is_unary_minus(i, inpt):
                if count % 2 == 0:
                    # Remove all consecutive minuses if the count is even
                    for _ in range(count):
                        inpt.pop(i)
                else:
                    # Reduce to a single minus if the count is odd
                    for _ in range(count - 1):
                        inpt.pop(i)
                    inpt[i]='_'
                    i += 1  # Move past the single remaining minus

            elif is_binary(i, inpt):
                if count % 2 == 0:
                    # If the count is even, keep the last two minuses
                    for _ in range(count - 2):
                        inpt.pop(i)
                else:
                    # If the count is odd, keep the last one minus
                    for _ in range(count - 1):
                        inpt.pop(i)
                i += 1  # Move past the remaining minus(es)

            else:
                # Handle other cases
                if count % 2 == 0:
                    # If the count is even, remove all minuses
                    for _ in range(count):
                        inpt.pop(i)
                else:
                    # If the count is odd, keep the last minus
                    for _ in range(count - 1):
                        inpt.pop(i)
                    inpt[i]='`'
                i += 1  # Move past the remaining minus

        else:
            i += 1

    return ''.join(inpt)

def main():
    user_input = input("Enter something: ")
    while user_input!='.':
        print(minus_destroyer(user_input))
        user_input = input("Enter something: ")



if __name__ == "__main__":
    main()