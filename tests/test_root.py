import math
import unittest

from menu import solve_square_equation


class TestSolveSquareEquation(unittest.TestCase):
    def test_with_positive_discriminant(self):
        a, b, c = 1, -3, 2
        expected_roots = (2.0, 1.0)
        actual_roots = solve_square_equation(a, b, c)
        self.assertEqual(actual_roots, expected_roots)

    def test_with_zero_discriminant(self):
        a, b, c = 1, 2, 1
        expected_roots = (-1.0, None)
        actual_roots = solve_square_equation(a, b, c)
        self.assertEqual(actual_roots, expected_roots)

    def test_with_negative_discriminant(self):
        a, b, c = 1, 2, 3
        expected_roots = (None, None)
        actual_roots = solve_square_equation(a, b, c)
        self.assertEqual(actual_roots, expected_roots)

    def test_with_zero_a(self):
        a, b, c = 0, 2, 3
        with self.assertRaises(ZeroDivisionError):
            solve_square_equation(a, b, c)


if __name__ == '__main__':
    unittest.main()
