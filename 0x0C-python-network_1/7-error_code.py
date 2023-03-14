#!/usr/bin/python3
"""This code checks the status code of a URL that is passed
in as an argument. If the status code is 400 or higher, it prints
an error message with the status code. If the status code
is lower than 400, it prints out the text from the URL.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
