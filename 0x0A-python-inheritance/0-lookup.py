#!/usr/bin/python3
""" file contaning a function lookup"""

def lookup(obj):
    """ a function that looks up all the attributes of an object"""
    objdict = [i for i in obj.__dict__]
    return objdict
    