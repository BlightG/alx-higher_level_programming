#!/usr/bin/python3
"""script that fetches a static URl"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
    response = req.read()
    print('Body response:')
    print(f'\ttype: {type(response)}')
    print(f'\tcontent: {response}')
    print(f'\tutf8 content:{response.decode("utf8")}')
