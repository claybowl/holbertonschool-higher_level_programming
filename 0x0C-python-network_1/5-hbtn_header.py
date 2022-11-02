#!/usr/bin/python3
"""script request to given url and displays value of variable X-Request-ID"""
import requests
from sys import argv

if __name__ == '__main__':
    givenurl = argv[1]
    response = requests.get(givenurl)
    print(response.headers.get('X-Request-Id'))
