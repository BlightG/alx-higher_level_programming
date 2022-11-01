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
        r2 = Rectangle(1, 2, 3, 4)
        dict = {'x': 3, 'y': 4, 'id': 4, 'height': 2, 'width': 1}
        self.assertEqual(r2.to_dictionary(), dict)
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(r3.id, 5)

    def test_rectangle_Exception(self):
        """ Checks the Exceptions for Rectangle """
        self.assertRaises(ValueError, Rectangle, 10, -2)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(ValueError, Rectangle, 10, 2, -4, 0)
