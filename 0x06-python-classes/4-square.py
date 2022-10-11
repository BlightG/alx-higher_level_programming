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
            raise Exception('size must be an integer')
        except ValueError as ve:
            raise Exception('size must be >= 0')

    def get_size(self):
        """ return size to user"""
        return self.__size

    def set_size(self, value):
        """ Set Size to value"""
        Square.__init__(self, value)

    def area(self):
        """ Define area of a Square"""
        area = self.__size ** 2
        return area

    size = property(get_size, set_size)
