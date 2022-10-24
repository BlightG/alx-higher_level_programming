#!/usr/bin/python3
""" file contaning a function lookup"""


def lookup(obj):
    """ a function that looks up all the attributes of an object"""
    objdict = [[method_name for method_name in dir(obj)]]
    return objdict
