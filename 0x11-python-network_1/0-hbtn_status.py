#!/usr/bin/python3
"""script that fetches a static URl"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
    response = req.read()
    print('Body response:')
    print(f'   - type: {type(response)}')
    print(f'   - content: {response}')
    print(f'   - utf8 content:{response.decode("utf8")}')
