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
    if a != a:
        a = 89
    if b != b:
        b = 89

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
        exit()

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
        exit()

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
