#!/usr/bin/python3
""" creats a a class that inhearits from list object """


class MyList(list):
    "a class that inherits list object"

    def print_sorted(self):
        """ a functioon to sort an int list"""
        maxlist = []
        temp = self[:]
        length = len(self)
        for i in range(length):
            maxlist.append(temp.pop(temp.index(min(temp))))

        print(maxlist)
