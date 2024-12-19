from customExceptions import LargeNumberException,SmallNumberException
def addition(first, second):
    return first + second

def subtraction(first, second):
    return first - second

def multiplication(first, second):
    return first * second

def division(first, second):
    return first / second

def power(first, second):
    return first ** second

def modulo(first,second):
    return first%second

def max_value(first, second):
    return first if first > second else second

def min_value(first, second):
    return first if first < second else second

def avg(first, second):
    return (first + second) / 2

def negative(num):
    return -num

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

def hashtag(num):
    num_str = str(num)
    print(num_str)
    is_negative = num_str.startswith('-')

    # Remove the minus sign if it exists
    if is_negative:
        num_str = num_str[1:]

    # Sum only the digits (ignore other characters like '.')
    total = sum(int(digit) for digit in num_str if digit.isdigit())

    # Return the sum as negative if the original number was negative
    return -total if is_negative else total
    '''
    f=False
    num_lst = list(str(num))
    num=0
    if num_lst[0]=="-":
        num_lst[0]=num_lst[0]*(-1)
        f=True
    for n in num_lst:#insted of using reduce
        num+=int(n)
    if f:
        return num*-1
    return num'''


def main():
    print(hashtag((input("enter number"))))
if __name__ == "__main__":
    main()



