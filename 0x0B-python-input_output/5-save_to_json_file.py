#!/usr/bin/python3
""" print json to string """
import json


def save_to_json_file(my_obj, filename):
    """ print my_obj to file @filename """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
