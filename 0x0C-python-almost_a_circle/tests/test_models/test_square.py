#!/usr/bin/python3
""" test module for Square """
import unittest
from models.square import Square



class TestRectangle(unittest.TestCase):
    """ A set of tests for Rectangle Class """
    def test_rectangle_Equal(self):
        """ Checks sucesses case of Base class """
        s1 = Square(10, 2)
        self.assertEqual(s1.id, 4)
        s2 = Square(10, 2, 0, 12)
        dict = {'x': 2, 'y': 0, 'id': 12, 'size': 10}
        self.assertEqual(s2.to_dictionary(), dict)

    def test_square_Exception(self):
        """ Checks the Exceptions for Rectangle """
        self.assertRaises(ValueError, Square, 10, -2)
        self.assertRaises(TypeError, Square)
        self.assertRaises(ValueError, Square, 10, 2, -4, 0)
