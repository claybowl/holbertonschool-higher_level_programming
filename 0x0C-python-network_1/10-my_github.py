#!/usr/bin/python3
"""This code is a Python script that takes two
command line arguments: a GitHub username and token.
It then uses the GitHub API to make a request for the
user's ID and prints it out. If the request fails,
it prints out "None".
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username, token = argv[1:]

    s = requests.Session()

    data = {'username': username, 'token': token}
    response = s.get(url, auth=(username, token)).json()
    try:
        print(response['id'])
    except:
        print('None')
