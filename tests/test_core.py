import unittest

from big_integer_square_root import isqrt


class TestIsqrt(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(isqrt(0), 0)

    def test_one(self):
        self.assertEqual(isqrt(1), 1)

    def test_two(self):
        self.assertEqual(isqrt(2), 1)

    def test_three(self):
        self.assertEqual(isqrt(3), 1)

    def test_four(self):
        self.assertEqual(isqrt(4), 2)

    def test_eight(self):
        self.assertEqual(isqrt(8), 2)

    def test_nine(self):
        self.assertEqual(isqrt(9), 3)

    def test_fifteen(self):
        self.assertEqual(isqrt(15), 3)

    def test_sixteen(self):
        self.assertEqual(isqrt(16), 4)

    def test_perfect_square_large(self):
        r = 10 ** 50 + 12345
        self.assertEqual(isqrt(r * r), r)

    def test_just_below_perfect_square(self):
        r = 10 ** 50 + 12345
        self.assertEqual(isqrt(r * r - 1), r - 1)

    def test_just_above_perfect_square(self):
        r = 10 ** 50 + 12345
        self.assertEqual(isqrt(r * r + 1), r)

    def test_huge_non_square(self):
        # A number around 10^200 whose root is not integer.
        n = 10 ** 200 + 7
        r = isqrt(n)
        self.assertLessEqual(r * r, n)
        self.assertLess(n, (r + 1) * (r + 1))

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            isqrt(-1)

    def test_result_type_is_int(self):
        self.assertIsInstance(isqrt(123456789), int)


if __name__ == "__main__":
    unittest.main()
