#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = 1
    summ = 0
    if len(sys.argv) > 1:
        while i < len(sys.argv):
            summ = summ + int(sys.argv[i])
            i += 1
    print("{}".format(summ))
