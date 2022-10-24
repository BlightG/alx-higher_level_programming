#!/usr/bin/python3
""" a module  for setting atribute to an object """


def add_attribute(obj, attr, val):
    """ a function that adds or modifies an attribute to an object
    
        Args:
            obj: object to be moodified
            attr: a string value of the attributw to be moddfied or added
            val: new value of the modifed attribute
        
        Return:
            returns an object with etra attribute
    """
    if not hasattr(obj, attr) and not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, val)






