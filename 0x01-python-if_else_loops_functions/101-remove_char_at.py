#!/usr/bin/python3
def remove_char_at(str, n):
    temp = (str + '.')[:-1]
    temp[n - 1] = ""
    return temp
