#!/usr/bin/python3
""" print json to string """
import json


def load_from_json_file(filename):
    """ print my_obj to file @filename """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
