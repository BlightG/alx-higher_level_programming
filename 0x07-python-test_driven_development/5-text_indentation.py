#!/usr/bin/python3

def text_indentation(text):
    
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print()
            print()
        else:
            print(i, end="")
        