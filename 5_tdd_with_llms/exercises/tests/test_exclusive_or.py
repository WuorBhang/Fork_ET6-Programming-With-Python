import unittest
from ..exclusive_or import exclusive_or


class TestExclusiveOr(unittest.TestCase):
    def test_str_in_list1(self):
        """It should return True if str is in list1 but not list2."""
        actual = exclusive_or('a', ['a', 'b'], ['c', 'd'])
        expected = True
        self.assertEqual(actual, expected)

    def test_str_in_list2(self):
        """It should return True if str is in list2 but not list1."""
        actual = exclusive_or('c', ['a', 'b'], ['c', 'd'])
        expected = True
        self.assertEqual(actual, expected)

    def test_str_in_both(self):
        """It should return True if str is in both lists."""
        actual = exclusive_or('a', ['a', 'b'], ['a', 'c'])
        expected = True
        self.assertEqual(actual, expected)

    def test_str_in_none(self):
        """It should return False if str is in neither list."""
        actual = exclusive_or('a', [], [])
        expected = False
        self.assertEqual(actual, expected)

    def test_str_in_list1_and_list2_empty(self):
        """It should return True if str is in list1 and list2 is empty."""
        actual = exclusive_or('a', ['a', 'b'], [])
        expected = True
        self.assertEqual(actual, expected)

    def test_str_in_list2_and_list1_empty(self):
        """It should return True if str is in list2 and list1 is empty."""
        actual = exclusive_or('a', [], ['a', 'b'])
        expected = True
        self.assertEqual(actual, expected)
