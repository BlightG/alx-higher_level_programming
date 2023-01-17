#!/usr/bin/python3
""" writes error code """
import requests
import sys


if __name__ == '__main__':
    try:
        response = requests.get(sys.argv[1])
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError:
        print(f'Error code: {response.status_code}')
