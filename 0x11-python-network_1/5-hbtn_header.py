#!/usr/bin/python3
"""send url and displays value of X-Request-Id"""
import sys
import requests


if __name__ == '__main__':
    with requests.get(sys.argv[1]) as response:
        header = response.headers
        print(header['X-Request-Id'])
