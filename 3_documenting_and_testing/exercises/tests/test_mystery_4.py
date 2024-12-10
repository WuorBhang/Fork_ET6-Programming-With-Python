import unittest
from ..mystery_4 import mystery_4


class TestMystery4(unittest.TestCase):
    def test_1(self):
        """It should return all instances of the integer 2."""
        actual = mystery_4([1, 2, 3, 4, 2, 5], 2)
        expected = [2, 2]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should return an empty list if no elements match."""
        actual = mystery_4([10, 20, 30, 40], 15)
        expected = []
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should return all elements if they all match the integer 5."""
        actual = mystery_4([5, 5, 5, 5], 5)
        expected = [5, 5, 5, 5]
        self.assertEqual(actual, expected)

    def test_4(self):
        """It should return an empty list if the input list is empty."""
        actual = mystery_4([], 1)
        expected = []
        self.assertEqual(actual, expected)

    def test_5(self):
        """It should return an empty list if `b` is not in the list."""
        actual = mystery_4([1, 2, 3, 4, 5], 6)
        expected = []
        self.assertEqual(actual, expected)
