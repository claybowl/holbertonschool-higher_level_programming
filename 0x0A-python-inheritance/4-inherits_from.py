#!/usr/bin/python3
"""Module 4-inherits_from
Returns True if obj is an instance of parent class
otherwise False
"""


def inherits_from(obj, a_class):
    """Tests if obj is instance of a_class parent class"""

    return isinstance(obj, a_class) and type(obj) != a_class

