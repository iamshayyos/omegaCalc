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

def max_value(first, second):
    return first if first > second else second

def min_value(first, second):
    return first if first < second else second

def avg(first, second):
    return (first + second) / 2


operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '^': power,
    '@': max_value,
    '$': min_value,
    '&': avg
}
