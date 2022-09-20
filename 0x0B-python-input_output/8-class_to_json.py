#!/usr/bin/python3
"""Module 3-class_to_json
Returns the dictionary description with simple data structure for JSON
serialization of an object
"""


def class_to_json(obj):
    """creates a dictionary description of object"""

    return obj.__dict__
