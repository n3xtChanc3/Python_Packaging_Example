import unittest
from calculations.addition import Addition
from calculations.subtraction import Subtraction
from calculations.multiplication import Multiplication
from calculations.division import Division

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        # Test addition
        addition = Addition(5, 3)
        self.assertEqual(addition.add(), 8)

    def test_subtraction(self):
        # Test subtraction
        subtraction = Subtraction(5, 3)
        self.assertEqual(subtraction.subtract(), 2)

    def test_multiplication(self):
        # Test multiplication
        multiplication = Multiplication(5, 3)
        self.assertEqual(multiplication.multiply(), 15)

    def test_division(self):
        # Test division
        division = Division(10, 2)
        self.assertEqual(division.divide(), 5)

        # Test division by zero
        division_by_zero = Division(10, 0)
        self.assertEqual(division_by_zero.divide(), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()
