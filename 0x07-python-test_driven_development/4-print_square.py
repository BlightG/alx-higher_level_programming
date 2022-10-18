#!/usr/bin/python3
""" a function that prints a square with side length equal to 
the user input size and raises exception if the input is 
not an int or less than 0
"""


def print_square(size):
    """ function that uses # character to print a square

        Args:
            size (int): an intal value for size of the square
        
        Return: 
            void 
    """
    if not isinstance(size, (int)):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print("#")
