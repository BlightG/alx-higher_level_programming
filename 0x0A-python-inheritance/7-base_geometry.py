#!/usr/bin/python3
""" started for base geometry"""


class BaseGeometry:
    """ Empty class base geomety"""
    def area(self):
        """ a module not yet implemented """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates if @value is a postive int"""
        
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.value = value
            self.name = name
