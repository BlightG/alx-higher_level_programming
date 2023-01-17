#!/usr/bin/python3
""" send a post to url and print reply """
import sys
import urllib.request
import urllib.parse


values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as responses:
    response = responeses.read()
    print(response)
