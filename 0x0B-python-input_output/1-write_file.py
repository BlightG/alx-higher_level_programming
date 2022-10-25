#!/usr/bin/python3
""" a function to count wrtie amount """


def write_file(filename="", text=""):
    ''' file length '''
    with open(filename, 'w', encoding='utf-8') as f:
        fcount = f.write(text)
        return fcount
