#!/usr/bin/python3
""" a module for checking is same """


def inherits_from(obj, a_class):
    """ checks if obk is instance of a_class """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
