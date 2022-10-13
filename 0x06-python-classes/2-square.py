#!/usr/bin/python3
""" Define a Square """


class Square:
    """ Define a Square"""
    def __init__(self, size=0):
        """ define a square size"""
        try:
            if size < 0:
                raise ValueError
            elif type(size) == float:
                raise TypeError
            else:
                self.__size = size
        except TypeError as te:
            raise Exception('size must be an integer')
        except ValueError as ve:
            raise Exception('size must be >= 0')
