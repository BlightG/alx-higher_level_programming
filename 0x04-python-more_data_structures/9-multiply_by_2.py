#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {i: x * 2 for i, x in a_dictionary.items()}
    return newdict
