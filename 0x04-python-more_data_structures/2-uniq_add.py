#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = my_list[:]
    newlist.sort()
    summ = newlist[0]
    for i in range(1, len(newlist)):
        if newlist[i] != newlist[i - 1]:
            summ = newlist[i] + summ
        else:
            continue
    return summ
