#!/usr/bin/python3
""" takes url argument and returns X-Request-Id value of header"""
import sys
import urllib.request


if len(sys.argv) == 2:
    reqst = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reqst) as url:
        header_dict = url.getheader('X-Request-Id')
        print(header_dict)
