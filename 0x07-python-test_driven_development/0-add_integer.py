#!/usr/bin/python3
"""a module for addint two integers or 
   two floats, if no value is given the value of
   b is assumed to be 98. if a or b are given
   the value of float they will be typecasted to int
"""


def add_integer(a, b=98):
    """ add_integer (a, b)
        returns the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError ('a must be an integer')
        exit()

    if not isinstance(b, (int, float)):
        raise TypeError ('b must be an integer')
        exit()

    if isinstance(a, float):
        a = int(a)
    
    if isinstance(b, float):
        b = int(b)
    
    return a + b

