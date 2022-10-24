#!/usr/bin/python3
""" module containging class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class that inherits from Basegeometry"""
    def __init__(self, width, height):
        """ initializes a rectangle"""
        try:
            BaseGeometry.integer_validator(self, "height", height)
            BaseGeometry.integer_validator(self, "width", width)
            self.__width = width
            self.__height = height
        except Exception as err:
            print(err)
