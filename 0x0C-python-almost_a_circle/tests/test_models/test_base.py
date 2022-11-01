#!/usr/bin/python3
""" test module for base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ test Class for base """
    def test_base_equal(self):
        """ checks sucess of Base class """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        str = Base.to_json_string(None)
        self.assertEqual(str, "[]")
        str = Base.to_json_string([])
        self.assertEqual(str, "[]")
        str = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(str, '[{"id": 12}]')
        str = Base.from_json_string(None)
        self.assertEqual(str, [])
        str = Base.from_json_string("[]")
        self.assertEqual(str, [])
        str = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(str, [{"id": 89}])