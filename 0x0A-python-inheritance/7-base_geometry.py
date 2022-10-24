#!/usr/bin/python3
""" started for base geometry"""


class BaseGeometry:
    """ Empty class base geomety"""
    def area(self):
        """ a module not yet implemented """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates if @value is a postive int"""
        self.value = value
        self.name = name
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.value))
