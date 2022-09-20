#!/usr/bin/python3
"""Module 6-load_from_json_file
Creates an object from a "JSON file"
"""


import json


def load_from_json_file(filename):
    """creates an object from JSON file"""

    with open(filename, 'r') as f:
        return json.load(f)
