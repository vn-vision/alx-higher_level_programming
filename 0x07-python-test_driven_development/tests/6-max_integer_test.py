#!/usr/bin/python3
""" TesCase script to test max_integer([..])
on unit level
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

# A testcase is created by subclassing unittest.TestCase


class TestMaxInteger(unittest.TestCase):

    """
    The unittest module provides tools for constructing and running tests
    test_ means it's a method
    assertEqual - compares the value returned by mas_integer
    to the expected (highest)value in the list
    in the case the list is empty , expect None
    """
    def test_upper(self):
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([2]), 2)

    def test_one_neg(self):
        self.assertEqual(max_integer([-10]), -10)

    def test_neg(self):
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

    def test_middle(self):
        self.assertEqual(max_integer([1, 3, 8, 2, 6]), 8)


if __name__ == '__main__':
    unittest.main()
