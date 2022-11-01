#!/usr/bin/python3
""" test module for base """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ A set of tests for Rectangle Class """
    def test_rectangle_Equal(self):
        """ Checks sucesses case of Base class """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(10, 2, 0, 0, 12)
        dict = {'x': 0, 'y': 0, 'id': 3, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), dict)

    def test_rectangle_Exception(self):
        """ Checks the Exceptions for Rectangle """
        self.assertRaises(TypeError, Rectangle, "1", "2", "3", "4")
        self.assertRaises(ValueError, Rectangle, 10, -2)
        self.assertRaises(ValueError, Rectangle, 0, -2)
        self.assertRaises(ValueError, Rectangle, 10, 2, -3, -4)
