#!/usr/bin/python3

import sys


def main():
    if len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif len(sys.argv) == 1:
        print("0 arguments")
    elif len(sys.argv) > 2:
        i = 1
        print("{} arguments:".format(len(sys.argv)))
        while i <= len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1 


if __name__ == '__main__':
    main()
