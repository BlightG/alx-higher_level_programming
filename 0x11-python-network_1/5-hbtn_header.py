#!/usr/bin/python3
"""send url and displays value of X-Request-Id"""
import sys
import requests


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(res.header.get('X-Request-Id'))
