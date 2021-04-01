import unittest
from evaluate_rpn import rpn


class TestEvaluateRpn(unittest.TestCase):

    def test_sum_of_two(self):
        self.assertEqual(2, rpn('1 1 +'))

    def test_sum_of_n(self):
        self.assertEqual(9, rpn('1 2 2 4 + + +'))

    def test_diff_of_two(self):
        self.assertEqual(0, rpn('1 1 -'))

    def test_diff_of_n(self):
        self.assertEqual(8, rpn('10 2 4 4 - - -'))

    def test_combination_of_sum_and_diff(self):
        self.assertEqual(3, rpn('2 1 + 3 - 3 +'))

    def test_multiplication_of_2(self):
        self.assertEqual(6, rpn('2 3 x'))

    def test_multiplication_of_n(self):
        self.assertEqual(48, rpn('2 3 4 2 1 x x x x'))

    def test_division_of_2(self):
        self.assertEqual(4, rpn('12 3 /'))

    def test_division_of_n(self):
        self.assertEqual(1, rpn('6 24 8 2 / / /'))

    def test_combination_of_multiplication_and_division_of_n(self):
        self.assertEqual(1, rpn('8 2 / 8 4 / 2 x /'))


if __name__ == '__main__':
    unittest.main()
