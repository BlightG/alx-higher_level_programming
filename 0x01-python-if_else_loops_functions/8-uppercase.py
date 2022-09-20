#!/usr/bin/pyton3

def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            print("{}".format(chr(ord(i) - 32)),end="")
        else:
            print("{}".format(i),end="")
    print()
