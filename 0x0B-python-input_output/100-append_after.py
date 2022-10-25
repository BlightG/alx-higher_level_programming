#!/usr/bin/python3
""" a module containing a file to split a word"""


def append_after(filename="", search_string="", new_string=""):
    """ a function to append a file """
    contents = ""
    with open(filename, 'r+', encoding="utf-8") as f:

        for line in f:
            contents += line
            if search_string in line:
                contents += new_string

        f.seek(0, 0)
        f.write(contents)
