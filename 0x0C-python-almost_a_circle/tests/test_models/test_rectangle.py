#!/usr/bin/python3
""" test module for base """
import unittest
import sys
import io

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
        self.assertEqual(r1.area(), 20)
        str = "[Rectangle] (3) 0/0 - 10/2"
        self.assertEqual(r1.__str__(), str)

    def test_rectangle_Print(self):
        """ checks for functions that print to stdout """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        r3 = Rectangle(3, 3, 0, 0, 15)
        r3.display()
        self.assertEqual(capturedOutput.getvalue(), "###\n###\n###\n")
        sys.stdout = sys.__stdout__ 
        #capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 
        r3.update(x=1)
        r3.display()
        self.assertEqual(capturedOutput.getvalue(), " ###\n ###\n ###\n")
        sys.stdout = sys.__stdout__


    def test_rectangle_Exception(self):
        """ Checks the Exceptions for Rectangle """
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertRaises(ValueError, Rectangle, 10, 2, -3, -4)
