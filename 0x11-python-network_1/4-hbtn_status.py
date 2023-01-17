#!/usr/bin/python3
""" python script that fetches a static url using request module """
import requests

if __name__ == '__main__':
    with requests.get('https://alx-intranet.hbtn.io/status') as responses:
        response = str(responses.text)
        print('Body response:')
        print(f'\t- type: {type(response)}')
        print(f'\t- content: {response}')
