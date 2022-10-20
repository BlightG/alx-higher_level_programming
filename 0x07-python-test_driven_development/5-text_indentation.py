#!/usr/bin/python3
""" This module has functions for the manupitaltion of text
the functions will work on the identation of texts
"""


def text_indentation(text):
    """the text_indentation function will take a string form the user
    and look for instances of , ? annd : and it will print
    Args:
        text (str): a unser input text

    Return:
        void
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        i = 0
        while i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[i])
                print()
                if text[i + 1] == " ":
                    i += 1
                    #print(i, end='')
            else:
                print(text[i], end="")
            i += 1
