#!/usr/bin/python3
""" a module for reading file """


def read_file(filename=""):
    """
        A module for reading a UTF-8  encoded file and prints to stdout

        Args:
            filename: the name of the file
            with or without file path as a string
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
