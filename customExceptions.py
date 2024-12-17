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


class MismatchedBracketsException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"MismatchedBracketsException: {self.args[0]}"

class EmptyBracketsException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"EmptyBracketsException: {self.args[0]}"


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

'''
class ZeroToThePowerZeroException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"ZeroToThePowerZeroException: {self.args[0]}"

class NegativeRootException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"NegativeRootException: {self.args[0]}"
'''
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



