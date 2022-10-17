#!/usr/bin/python3
""" Define a square """


class Rectangle:
    """ a Class representing a rectangle """
    def __init__(self, width=0, height=0):
        """ an instantiation function"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def height(self):
        """ Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the value of the height """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the value of the width """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
