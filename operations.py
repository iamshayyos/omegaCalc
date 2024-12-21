
"""
operations.py

This module contains functions to perform basic mathematical operations.
It includes functions for addition, subtraction, multiplication, division,
modulo, power calculations, and other utility functions like max, min, average,
and factorial.
"""


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
    return str(-float(num))

def factorial(num):
    num=float(num)
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)


def hashtag(num):
    num_str = str(num)

    # Check if the number is negative
    is_negative = num_str.startswith('-')

    # Sum the digits (ignoring non-digit characters)
    total = sum(int(digit) for digit in num_str if digit.isdigit())

    # Return the sum as negative if the original number was negative
    return -total if is_negative else total


def main():
    print(hashtag((input("enter number"))))
if __name__ == "__main__":
    main()