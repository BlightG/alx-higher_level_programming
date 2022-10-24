#!/usr/bin/python3
""" file contaning a function lookup"""

def lookup(obj):
    objdict = [i for i in obj.__dict__]
    return objdict
    