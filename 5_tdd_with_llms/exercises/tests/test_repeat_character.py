import unittest
from ..repeat_character import repeat_character


class TestRepeatCharacter(unittest.TestCase):
    def test_repeat_character(self):
        """It should correctly repeat the character in the string."""
        actual = repeat_character("hello", "l", 2)
        expected = "hellllo"
        self.assertEqual(actual, expected)

    def test_repeat_character_multiple_appearance(self):
        """It should correctly repeat the character in the string when it appears multiple times."""
        actual = repeat_character("hello world", "l", 2)
        expected = "hellllo worlld"
        self.assertEqual(actual, expected)

    def test_repeat_character_not_in_string(self):
        """It should return the original string when the character is not present in the string."""
        actual = repeat_character("hello", "x", 2)
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_repeat_character_empty_string(self):
        """It should return an empty string when the input string is empty."""
        actual = repeat_character("", "l", 2)
        expected = ""
        self.assertEqual(actual, expected)

    def test_repeat_character_n_zero(self):
        """It should return the original string when n is zero."""
        actual = repeat_character("hello", "l", 0)
        expected = "hello"
        self.assertEqual(actual, expected)
