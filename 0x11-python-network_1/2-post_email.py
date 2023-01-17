#!/usr/bin/python3
""" send a post to url and print reply """
import sys
import urllib.request
# import urllib.parse


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as responses:
        response = responses.read()
        print(response.decode("utf8"))
