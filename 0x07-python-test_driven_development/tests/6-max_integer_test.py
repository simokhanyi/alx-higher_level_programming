#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Max of [1, 2, 3, 4] 4")
        self.assertEqual(max_integer([1, 3, 4, 2]), 4, "Max of [1, 3, 4, 2] 4")

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1,)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1,)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4,)
        self.assertEqual(max_integer([-4, 3, -2, 1]), 3,)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5, "Max of [5] 5")

    def test_duplicate_max(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5, "Max of [5, 5, 5, 5] 5")


if __name__ == "__main__":
    unittest.main()
