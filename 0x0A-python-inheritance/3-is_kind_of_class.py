#!/usr/bin/python3
"""Module 3-is_kind_of_class
Returns True if object is an instance of child
or parent class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Discovers if obj is instance of a_class or its parent class"""
    pass

    return True if type(obj) is a_class or super(a_class) else False
