#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def single_int_test(self):
        """tests single integer list"""
        v1 = [36]
        self.assertEqual(max_integer(v1), 36)

    def multi_int_test(self):
        """test multi integer list"""
        v1 = [2, 3, 5, 8, 13, 21, 34]
        test = max_integer(v1)
        self.assertEqual(test, 34)

    def not_int_test(self):
        """testing for non integer"""
        v1 = [2, 3, 5, "hi", 13, 21, 34]
        test = max_integer(v1)
        self.assertRaises(TypeError, max_integer, test)


if __name__ == '__main__':
    unittest.main()
