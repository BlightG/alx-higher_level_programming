#!/usr/bin/python3
""" module containging class Square"""
from turtle import width


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class that inherits from Rectangle"""
    def __init__(self, size):
        """ instansiation for objects of class """
        try:
            Rectangle.integer_validator(self, "size", size)
            self.__size = size
        except Exception as err:
            print(err)

        super().__init__(size, size)

    def area(self):
        """ calculates area of a rectangle """
        return self.__size ** 2
