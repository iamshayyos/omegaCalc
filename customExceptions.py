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


class ZeroToThePowerZeroException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"ZeroToThePowerZeroException: {self.args[0]}"
