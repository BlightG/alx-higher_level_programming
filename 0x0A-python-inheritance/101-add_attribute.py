#!/usr/bin/python3
""" a module  for setting atribute to an object """


def add_attribute(obj, attr, val):

    if not hasattr(obj, attr) and not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, val)






