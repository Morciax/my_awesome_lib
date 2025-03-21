import unittest
from my_awesome_lib.math_tools import factorial, MathOperations

class TestMathOperations(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)  # 0! = 1
        self.assertEqual(factorial(1), 1)  # 1! = 1
        self.assertEqual(factorial(5), 120)  # 5! = 120

    def test_gcd(self):
        self.assertEqual(MathOperations.gcd(48, 18), 6)  # NWD(48,18) = 6
        self.assertEqual(MathOperations.gcd(101, 103), 1)  # Liczby pierwsze -> NWD = 1
        self.assertEqual(MathOperations.gcd(56, 98), 14)  # NWD(56,98) = 14
        self.assertEqual(MathOperations.gcd(10, 0), 10)  # NWD(a, 0) = a

if __name__ == "__main__":
    unittest.main()
