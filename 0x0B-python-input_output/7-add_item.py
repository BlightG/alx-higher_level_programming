#!/usr/bin/python3
""" a function to add argumetns to a list """
from importlib.resources import path
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
#read_file = __import__("0-read_file").read_file

def write_to_json():
    """ a function to write a to json """
    if not os.path.exists('add_item.json'):
        my_list = []
        print("not exist")
        with open('add_item.json', 'w+', encoding='utf-8') as f:
            save_to_json_file(my_list, 'add_item.json')
    
    mylist = load_from_json_file('add_item.json')
    for i in range(1, len(sys.argv)):
        mylist.append(sys.argv[i])
        print(mylist)
    save_to_json_file(mylist, 'add_item.json')

write_to_json()
