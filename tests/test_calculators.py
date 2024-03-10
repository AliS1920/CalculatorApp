import unittest
from ..operations.arithmetic_operations import calculate


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(4, 3, 1), 7)

    def test_subtraction(self):
        self.assertEqual(calculate(8, 5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(calculate(6, 7, 3), 42)

    def test_division(self):
        self.assertEqual(calculate(10, 2, 4), 5)
        self.assertIsNone(calculate(10, 0, 4))

    def test_module(self):
        self.assertEqual(calculate(4, 2, 5), 0)


# this command is optional for console
if __name__ == '__main__':
    unittest.main()
