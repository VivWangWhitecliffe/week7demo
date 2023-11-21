import unittest
from app import Calculator 


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(8, 3)
        self.assertEqual(result, 5)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(4, 2)
        self.assertEqual(result, 8)

    def test_divide_valid(self):
        calculator = Calculator()
        result = calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        calculator = Calculator()
        result = calculator.divide(8, 0)
        self.assertEqual(result, "Cannot divide by zero")



if __name__ == '__main__':
    unittest.main()

