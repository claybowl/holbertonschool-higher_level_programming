#!/usr/bin/python3
"""Python script that uses the requests library to make
an HTTP request to the given URL (passed in as argument)
and then prints out the value of the X-Request-Id header
from the response.
"""
import requests
from sys import argv

if __name__ == '__main__':
    givenurl = argv[1]
    response = requests.get(givenurl)
    print(response.headers.get('X-Request-Id'))
