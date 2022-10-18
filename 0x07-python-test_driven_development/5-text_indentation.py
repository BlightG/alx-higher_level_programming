#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        for i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print()
                print()
            else:
                print(text[i], end="")
