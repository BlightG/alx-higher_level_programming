#!/usr/bin/python3
def common_elements(set_1, set_2):
    mylist = [j for i in set_2 if i in set_1]
    return mylist
