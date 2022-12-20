#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list[:]
    my_list.clear()
    for i in range(len(new_list)):
        if i != idx:
            my_list.append(new_list[i])
    return my_list
