#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    hiddir = dir(hidden_4)
    for i in range(0, len(hiddir)):
        if hiddir[i][0] != "_":
            print("{}".format(hiddir[i]))
