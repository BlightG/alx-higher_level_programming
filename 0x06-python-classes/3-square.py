#!/usr/bin/python3
""" Define a Square """


class Square:
    """ Define a Square"""
    def __init__(self, size=0):
        """ define a square size"""
        try:
            if size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError as te:
            print('size must be an integer', end="")
            raise Exception
        except ValueError as ve:
            print('size must be >= 0', end="")
            raise Exception

    def area(self):
        """ Define area of a Square"""
        area = self.__size ** 2
        return area
