#!/usr/bin/python3
"""This code uses the urllib.request module
to open a URL and read its contents. It then prints
out the type of response, the content of the
response, and the utf-8 encoded content
of the response.
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
