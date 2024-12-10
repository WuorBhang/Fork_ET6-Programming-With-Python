import unittest
from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    def test_1(self):
        """It should correctly sort a list of integers."""
        actual = mystery_3([5, 3, 8, 6, 2])
        expected = [2, 3, 5, 6, 8]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should return the same list if it is already sorted."""
        actual = mystery_3([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should correctly sort a list with negative integers."""
        actual = mystery_3([10, -2, 4, 3])
        expected = [-2, 3, 4, 10]
        self.assertEqual(actual, expected)

    def test_4(self):
        """It should return an empty list if the input is empty."""
        actual = mystery_3([])
        expected = []
        self.assertEqual(actual, expected)

    def test_5(self):
        """It should return the same list if it contains a single element."""
        actual = mystery_3([9])
        expected = [9]
        self.assertEqual(actual, expected)

