#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        sys.stderr.write("Exception: {}".format(error))
        return False