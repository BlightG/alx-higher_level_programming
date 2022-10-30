#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test """
    def test_int_list(self):
        self.assertEqual(max_integer([1, 2, 6]), 6)
        self.assertEqual(max_integer([1, 6, 2]), 6)
        self.assertEqual(max_integer([-1, -3]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)

    def test_invalid_list(self):
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 4, "str"])
        self.assertRaises(TypeError, max_integer, [1, (2, 1), 3, 4])
