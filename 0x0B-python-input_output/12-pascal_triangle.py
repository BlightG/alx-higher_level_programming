#!/usr/bin/python3
""" a solution to pascals triangle """


def pascal_triangle(n):
    """ pascals triangle """
    mylist = []
    temp = []
    # if n is <+= 0  return an empty list
    if n <= 0:
        return mylist

    # initialize mylist as a triangle
    mylist = [[0 for i in range(j)] for j in range(1, n + 1)]

    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            if j == 0 or j == len(mylist[i]) - 1:
                mylist[i][j] = 1
            else:
                mylist[i][j] = temp[j] + temp[j - 1]

        temp = mylist[i]

    return mylist
