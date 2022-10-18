#!/usr/bin/python3
""" this is a very simple module that has one function
to print a string and prior to printing it conacts some user 
supplied  string to it
"""


def say_my_name(first_name, last_name=""):
    """ a function that prints a string after inserting strings from user

        Args:
            first_name (str): first string, doesnnt have a deafault string
            last_name (str): second string, has an empty string as a default
        
        Return:
            void
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("my name is {} {}".format(first_name, last_name))
