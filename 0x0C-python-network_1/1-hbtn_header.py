#!/usr/bin/python3
"""This code is a Python script that takes
a URL as an argument and sends a request to the URL.
It then displays the value of the X-Request-ID
header from the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers['X-Request-Id']

    print(x_request_id)
