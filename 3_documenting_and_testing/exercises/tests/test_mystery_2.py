import unittest
from ..mystery_2 import mystery_2

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
<<<<<<< HEAD
    def test_1(self):
        """It should return elements containing the integer `3`."""
        actual = mystery_2([[1, 2, 3], [4, 5], [3, 6, 7]], 3)
        expected = [[1, 2, 3], [3, 6, 7]]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should return elements containing the digit `4`."""
        actual = mystery_2([123, 456, 789], 4)
        expected = [456]
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should return an empty list when input list is empty."""
        actual = mystery_2([], 3)
        expected = []
        self.assertEqual(actual, expected)

    def test_4(self):
        """It should return an empty list if no elements contain `7`."""
        actual = mystery_2([[1, 2], [3, 4], [5, 6]], 7)
        expected = []
        self.assertEqual(actual, expected)

    def test_5(self):
        """It should return elements containing the integer `20`."""
        actual = mystery_2([10, 20, 30, 40], 20)
        expected = [20]
        self.assertEqual(actual, expected)
=======
    """ """

    def test_minimal_list_input(self):
        """"""
        self.assertEqual(mystery_2([]), None)

    def test_minimal_string_input(self):
        """"""
        self.assertEqual(mystery_2(''), None)
>>>>>>> 493fa105c419abe6ff758942e2cce0e36388e008
