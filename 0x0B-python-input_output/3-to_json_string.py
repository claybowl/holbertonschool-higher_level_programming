#!/usr/bin/python3
"""Module 3-to_json_string.py
Returns JSON representation of an object(string)
"""


import json

def to_json_string(my_obj):
    """returns the JSON representation of object"""

    return json.dumps(my_obj)
