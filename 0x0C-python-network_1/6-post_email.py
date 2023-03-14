#!/usr/bin/python3
"""Script that uses the request module to post an
email to a given URL. It takes two command line arguments,
the URL and the email address., and sends a POST request with
the email as data. It then prints out the response
text from the server.
"""
from sys import argv
import requests


if __name__ == '__main__':
    givenurl = argv[1]
    givenemail = argv[2]
    response = requests.post(givenurl, data={'email': givenemail})
    print(response.text)
