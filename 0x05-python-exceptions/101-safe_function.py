#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as error:
        print("Exception : {}".format(error), file=sys.stderr)
        return None
