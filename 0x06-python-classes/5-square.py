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

    def my_print(self):
        """ Prints a Square """
        if self.__size != 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print('#', end="")
                print()
        else:
            print()

    size = property(get_size, set_size)
