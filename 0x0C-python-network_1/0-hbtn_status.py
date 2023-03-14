#!/usr/bin/env python3
"""0-hbn_status.py"""
import urllib.request


url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html = response.read()

print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode('utf-8'))
