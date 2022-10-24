#!/usr/bin/python3
""" creats a a class that inhearits from list object """


class MyList(list):
    "a class that inherits list object"
    def __init__(self, my_list=[]):
        """ initializes the object for Mylist"""
        self.my_list = my_list
        super().__init__(my_list)
    
    def print_sorted(self):
        maxlist = []
        length = len(self.my_list)
        print(length)
        for i in range(length):
            print(i)
            maxlist.append(self.my_list.pop(max(self.my_list)))
                
        print(length)
