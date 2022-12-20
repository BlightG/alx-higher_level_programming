#!/usr/bin/python3
""" a module for checking is same """


def is_same_class(obj, a_class):
    """ checks if obk is instance of a_class """
    if type(obj) is a_class:
        return True
    else:
        return False
