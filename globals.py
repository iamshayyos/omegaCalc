"""
globals.py

This module defines global constants used across the mathematical expression
processing and validation functions. It includes sets of supported operators,
operator priorities, and mappings to their corresponding functions.
"""
from operations import *

operators_no_repeat = {'+', '*', '/', '^', '%', '@', '$', '&', '~'}
supported_operators = {'+', '-', '*', '/', '^', '%', '&', '$', '@', '!', '~','#'}
valid_for_unary = {'+', '-', '*', '/', '^', '(', '~'}
binary_operators = {'+', '*', '/', '^', '%', '@', '$', '&'}
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
    "#":hashtag
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