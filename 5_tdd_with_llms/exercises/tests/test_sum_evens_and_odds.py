import unittest
from ..sum_evens_and_odds import sum_evens_and_odds


class TestSumEvensAndOdds(unittest.TestCase):
    def test_sum_evens_and_odds(self):
        """It should correctly calculate the sum of even and odd numbers in a list."""
        numbers = [1, 2, 3, 4, 5, 6]
        actual = sum_evens_and_odds(numbers)
        expected = {"even": 12, "odd": 9}
        self.assertEqual(actual, expected)

    def test_sum_evens_and_odds_empty_list(self):
        """It should return a dictionary with zeros for an empty list."""
        numbers = []
        actual = sum_evens_and_odds(numbers)
        expected = {"even": 0, "odd": 0}
        self.assertEqual(actual, expected)

    def test_sum_evens_and_odds_all_even(self):
        """It should correctly calculate the sum of even numbers in a list with only even numbers."""
        numbers = [2, 4, 6, 8, 10]
        actual = sum_evens_and_odds(numbers)
        expected = {"even": 30, "odd": 0}
        self.assertEqual(actual, expected)

    def test_sum_evens_and_odds_all_odd(self):
        """It should correctly calculate the sum of odd numbers in a list with only odd numbers."""
        numbers = [1, 3, 5, 7, 9]
        actual = sum_evens_and_odds(numbers)
        expected = {"even": 0, "odd": 25}
        self.assertEqual(actual, expected)

    def test_sum_evens_and_odds_negative_numbers(self):
        """It should correctly calculate the sum of even and odd numbers in a list with negative numbers."""
        numbers = [-1, -2, -3, -4, -5, -6]
        actual = sum_evens_and_odds(numbers)
        expected = {"even": -12, "odd": -9}
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
