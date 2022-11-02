#!/usr/bin/python3
"""script takes & sends request to URL & displays value of X-Request-ID"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers['X-Request-Id'])
