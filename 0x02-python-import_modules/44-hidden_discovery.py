#!/usr/bin/python3
if __name__ == '__main__':
    import add_0
    hiddir = dir(add_0)
    for i in range(0, len(hiddir)):
        if hiddir[i][0] != "_":
            print("{}".format(hiddir[i]))
