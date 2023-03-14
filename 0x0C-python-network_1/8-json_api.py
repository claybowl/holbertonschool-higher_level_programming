#!/usr/bin/python3
""" It takes an argument from the command line (sys.argv[1])
and sends it as a payload to a server at 0.0.0.0:5000/search_user
via a POST request. It then tries to parse the response as
JSON and prints out either "No result" if the response is empty
or "[id] name" if it contains valid data. If it fails to parse
the response as JSON, it prints "Not a valid JSON".
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
