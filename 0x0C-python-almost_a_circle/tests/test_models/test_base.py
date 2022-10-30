#!/usr/bin/python3
""" test module for base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ test Class for base """
    def test_base_equal(self):
        """ checks sucess of Base class """
        b1 = Base()
        self.assertEquals(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEquals(b3.id, 2)
