import unittest
from manager import calculate
from customExceptions import *

class TestCalculator(unittest.TestCase):

    def assert_calculation(self, expression, expected_output):
        try:
            print(f"Testing: {expression}")
            result = calculate(expression)
            self.assertEqual(result, expected_output)  # Check if the result matches the expected output
        except Exception as e:
            self.fail(f"Test failed for input '{expression}' with exception: {e}")

    def assert_raises_exception(self, expression, exception_type):
        with self.assertRaises(exception_type):
            print(f"Testing for exception: {expression}")
            calculate(expression)

    # Basic tests
    def test_basic_addition(self):
        self.assert_calculation("2+3", 5)

    def test_basic_subtraction(self):
        self.assert_calculation("10-7", 3)

    def test_basic_multiplication(self):
        self.assert_calculation("4*5", 20)

    def test_basic_division(self):
        self.assert_calculation("8/2", 4)

    def test_power(self):
        self.assert_calculation("2^3", 8)

    # Edge cases
    def test_unary_minus(self):
        self.assert_calculation("-5", "-5")

    def test_multiple_unary_minuses(self):
        self.assert_calculation("--5", "5")

    def test_expression_with_parentheses(self):
        self.assert_calculation("(2+3)*4", 20)

    def test_expression_with_hashtag(self):
        self.assert_calculation("123#", 6)

    def test_expression_with_negative_hashtag(self):
        self.assert_raises_exception("(-123)#", HashtagException)

    def test_expression_with_factorial(self):
        self.assert_calculation("5!", 120)

    def test_expression_with_invalid_factorial(self):
        self.assert_raises_exception("(-5)!", InvalidFactorialException)

    # Error tests
    def test_division_by_zero(self):
        self.assert_raises_exception("5/0", ZeroDivisionError)

    def test_unmatched_parentheses(self):
        self.assert_raises_exception("(2+3", BracketsException)

    def test_repeating_signs(self):
        self.assert_raises_exception("2++3", RepeatingSigneException)

    def test_invalid_character(self):
        self.assert_raises_exception("2+3a", UnexpectedCharacterException)

    def test_large_number(self):
        self.assert_raises_exception("10^1000", LargeNumberException)

    def test_empty_input(self):
        self.assert_raises_exception("    ", AllWhiteSpaceException)


if __name__ == "__main__":
    unittest.main()
