#!/usr/bin/python3
"""script to post an email using requests module & given url and email"""
from sys import argv
import requests


if __name__ == '__main__':
    givenurl = argv[1]
    givenemail = argv[2]
    response = requests.post(givenurl, data={'email': givenemail})
    print(response.text)
