from operations import *

operators_no_repeat = {'+', '*', '/', '^', '%', '@', '$', '&', '~'}
supported_operators = {'+', '-', '*', '/', '^', '%', '&', '$', '@', '!', '~'}

# Operator priorities for parsing expressions
operator_priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    "%": 4,
    "@": 5,
    "$": 5,
    "&": 5,
    "~": 6,
    "!": 6,
    "#":6
}

# Operators mapped to their corresponding functions
operator_functions = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "^": power,
    "%": modulo,
    "@": avg,
    "$": max_value,
    "&": min_value,
    "~": negative,
    "!": factorial
}

# Number of operands each operator requires
operator_operands = {
    "+": 2,
    "-": 2,
    "*": 2,
    "/": 2,
    "^": 2,
    "%": 2,
    "@": 2,
    "$": 2,
    "&": 2,
    "~": 1,
    "!": 1
}