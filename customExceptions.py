"""
customExceptions.py

This module defines custom exception classes used for handling various errors
in mathematical expression validation and processing. Each exception class
includes a descriptive name and a custom `__str__` method to provide detailed
error messages.

The exceptions include:
- AllWhiteSpaceException: Raised when the input contains only whitespace.
- InvalidDotPlacementException: Raised for invalid dot placements in numbers.
- UnexpectedCharacterException: Raised when an unexpected character is found.
- BracketsException: Raised for unmatched or incorrectly placed parentheses.
- InvalidFactorialException: Raised when the factorial operator is used incorrectly.
- InvalidTildeException: Raised for incorrect placement of the tilde '~' operator.
- PowerException: Raised for invalid power operations (e.g., 0^0).
- RepeatingSigneException: Raised when consecutive repeating operators are found.
- MissingOperandsException: Raised when an operator is missing operands.
- HashtagException: Raised for incorrect usage of the hashtag '#' operator.
- LargeNumberException: Raised when a number is too large to process.
- SmallNumberException: Raised when a number is too small to process.
"""

class AllWhiteSpaceException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"AllWhiteSpaceException: {self.args[0]}"


class InvalidDotPlacementException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"InvalidDotPlacementException: {self.args[0]}"


class UnexpectedCharacterException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"UnexpectedCharacterException: {self.args[0]}"



class BracketsException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"BracketsException: {self.args[0]}"


class InvalidFactorialException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"InvalidFactorialException: {self.args[0]}"


class InvalidTildeException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"InvalidTildeException: {self.args[0]}"

class PowerException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"PowerZeroException: {self.args[0]}"

class RepeatingSigneException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"RepeatingSigneException: {self.args[0]}"

class MissingOperandsException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"MissingOperandsException: {self.args[0]}"

class HashtagException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"HashtagException: {self.args[0]}"


class LargeNumberException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"TooLargeNumberException: {self.args[0]}"

class SmallNumberException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"TooLargeNumberException: {self.args[0]}"



