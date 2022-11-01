#!/usr/bin/python3
""" test module for Square """
import unittest
from models.square import Square



class TestRectangle(unittest.TestCase):
    """ A set of tests for Rectangle Class """
    def test_rectangle_Equal(self):
        """ Checks sucesses case of Base class """
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Square(10, 2, 0, 12)
        dict = {'x': 0, 'y': 0, 'id': 1, 'size': 2}
        self.assertEqual(r1.to_dictionary(), dict)

    def test_square_Exception(self):
        """ Checks the Exceptions for Rectangle """
        self.assertRaises(ValueError, Square, 10, -2)
        self.assertRaises(TypeError, Square)
        self.assertRaises(ValueError, Square, 10, 2, -4, 0)
