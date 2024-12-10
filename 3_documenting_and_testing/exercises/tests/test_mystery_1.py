import unittest
from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    def test_1(self):
        """It should correctly sort a list of integers."""
        actual = mystery_1([5, 3, 8, 6, 2])
        expected = [2, 3, 5, 6, 8]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should return the same list if it is already sorted."""
        actual = mystery_1([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should correctly sort a list with negative integers."""
        actual = mystery_1([10, -2, 4, 3])
        expected = [-2, 3, 4, 10]
        self.assertEqual(actual, expected)

    def test_4(self):
        """It should return an empty list if the input is empty."""
        actual = mystery_1([])
        expected = []
        self.assertEqual(actual, expected)

    def test_5(self):
        """It should return the same list if it contains a single element."""
        actual = mystery_1([9])
        expected = [9]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
