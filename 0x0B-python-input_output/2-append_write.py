#!/usr/bin/python3
""" a function for printing and counting """


def append_write(filename="", text=""):
    """ function for appending """
    with open(filename, 'a', encoding='utf-8')as f:
        f.seek(0, 2)
        fcount = f.write(text)
        return fcount
