#!/usr/bin/python3
""" print json to string """
import json


def load_from_json_file(filename):
    """ print my_obj to file @filename """
    with open(filename, 'r', encoding='utf-8') as f:
        if f.read() != 0:
            f.seek(0, 0)
            return json.loads(f.read())
