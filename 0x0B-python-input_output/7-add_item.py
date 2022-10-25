#!/usr/bin/python3
""" a function to add argumetns to a list """
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def write_to_json():
    """ a function to write a to json """
    if not os.path.exists('add_item.json'):
        mylist = []
        with open('add_item.json', 'w+', encoding='utf-8'):
            save_to_json_file(mylist, 'add_item.json')

    mylist = load_from_json_file('add_item.json')
    for i in range(1, len(sys.argv)):
        mylist.append(sys.argv[i])
    save_to_json_file(mylist, 'add_item.json')


write_to_json()
