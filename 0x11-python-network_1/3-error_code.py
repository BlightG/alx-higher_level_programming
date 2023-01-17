#!/usr/bin/python3
""" send s requespt and prints response body while managing error """
import urllib.request
import sys
import urllib.error


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as responses:
            print(responses.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
