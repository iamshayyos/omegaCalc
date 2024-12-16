from operations import *

operators_no_repeat = {'+', '*', '/', '^', '%', '@', '$', '&', '~'}
supported_operators = {'+', '-', '*', '/', '^', '%', '&', '$', '@', '!', '~'}
valid_for_unary = {'+', '-', '*', '/', '^', '(', '~'}
# Operator priorities for parsing expressions
operator_priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "_": 2.5,#unary minus
    "^": 3,
    "%": 4,
    "@": 5,
    "$": 5,
    "&": 5,
    "~": 6,
    "!": 6,
    "#": 6,
    "`": 7#sign minus
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
    "!": factorial,
    "`": lambda x: -x,
    "#":hash_addition
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
    "!": 1,
    "`": 1,
    "#":1
}