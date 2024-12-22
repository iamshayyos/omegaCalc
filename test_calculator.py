"""
test_calculator.py

This module contains unit tests for the `calculate` function in `manager.py`.
It verifies the correctness of mathematical expression calculations and ensures
proper exception handling for various edge cases and invalid inputs.

The tests include:
- Basic arithmetic operations (addition, subtraction, multiplication, division, power)
- Complex expressions with multiple operators and parentheses
- Edge cases such as unary minus and multiple unary minuses
- Factorial calculations and hashtag operations
- Exception handling for errors such as:
  - Division by zero
  - Invalid characters
  - Repeating signs
  - Unmatched parentheses
  - Invalid factorial usage
  - Large numbers and power exceptions
  - Empty or whitespace-only inputs

To run the tests, execute this file directly with Python's `unittest` framework:python test_calculator.py or from the run button placed on the upper navbar
"""

import unittest
from manager import calculate
from customExceptions import *

class TestCalculator(unittest.TestCase):

    def assert_calculation(self, expression, expected_output):
        try:
            print(f"Testing: {expression}")
            result = calculate(expression)
            self.assertAlmostEqual(result, expected_output, places=7)  # Check with tolerance
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

    def test_precession(self):
        self.assert_calculation("10-9.9",0.1)

    def test_complicate_input(self):
        self.assert_calculation("((3 + 5*2)^2)/4 + (12*2 $ 5*3) - (10/2 & 7) + 4! + 9@3@6 + 123# * (23%5) - ~8", 273.25)


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

    def test_negative_hashtag(self):
        self.assert_raises_exception("(-5)#", HashtagException)

    def test_empty_parentheses(self):
        self.assert_raises_exception("5+()+2", BracketsException)

    def test_repeating_signs(self):
        self.assert_raises_exception("2++3", RepeatingSigneException)

    def test_invalid_character(self):
        self.assert_raises_exception("2+3a", UnexpectedCharacterException)

    def test_large_number(self):
        self.assert_raises_exception("10^1000", LargeNumberException)

    def test_zero_to_the_power_of_zero(self):
        self.assert_raises_exception("(1-0!)^(0%100)", PowerException)

    def test_root_of_negative_number(self):
        self.assert_raises_exception("(-2)^(0.5)", PowerException)

    def test_empty_input(self):
        self.assert_raises_exception("    ", AllWhiteSpaceException)






if __name__ == "__main__":
    unittest.main()
