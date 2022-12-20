#!/usr/bin/python3
def no_c(my_string):
    my_list = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            my_list = my_list + my_string[i]
    return my_list
