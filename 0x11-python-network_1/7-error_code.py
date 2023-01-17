#!/usr/bin/python3
""" writes error code """
import requests
import sys


if __name__ == '__main__':
    try:
        response = requsets.get(sys.argv[1])
        print(response.txt)
    except HTTPError:
        print(response.status_code)
