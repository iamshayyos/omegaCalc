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


def main():
    print(factorial(int(input("enter number"))))
if __name__ == "__main__":
    main()



