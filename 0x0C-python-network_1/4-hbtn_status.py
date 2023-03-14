#!/usr/bin/python3
"""Python script that uses the ruequests library to fetch
the status of the URL https://intranet.hbtn.io/status. It then
prints out the type and content of the response from the request.
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(req.text)))
    print('\t- content: {_content}'.format(_content=req.text))
