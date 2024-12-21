"""
globals.py

This module defines global constants used across the mathematical expression
processing and validation functions. It includes sets of supported operators,
operator priorities, and mappings to their corresponding functions.
"""
from operations import *

OPERATORS_NO_REPEAT = {'+', '*', '/', '^', '%', '@', '$', '&', '~'}
SUPPORTED_OPERATORS = {'+', '-', '*', '/', '^', '%', '&', '$', '@', '!', '~','#'}
VALID_FOR_UNARY = {'+', '-', '*', '/', '^', '(', '~'}
BINARY_OPERATORS = {'+', '*', '/', '^', '%', '@', '$', '&'}
# Operator priorities for parsing expressions
OPERATOR_PRIORITY = {
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
OPERATOR_FUNCTIONS = {
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
    "#":hashtag
}

# Number of operands each operator requires
OPERATOR_OPERANDS = {
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