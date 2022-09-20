#!/usr/bin/python3

def uppercase(str):
    str = str + "\n"
    for i in str:
        if ord(i) in range(97, 123):
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
