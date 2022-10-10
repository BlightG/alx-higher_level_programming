#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as error:
        print("Exception : {}".format(error), file=sys.stderr)
        return None
