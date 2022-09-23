#!/usr/bin/python3
"""Module base.py
Base class for for all project classes

"""


import json


class Base:
    """base class for geometric objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


def integer_validator(value, num):
    """validate that num is an integer"""

    if type(value) is not str:
        raise TypeError("value passed to validate_int must be string")
    if type(num) is not int:
        raise TypeError(f"{value} must be an integer")
    if num <= 0:
        raise ValueError(f"{value} must be > 0")


def no_neg_validator(value, num):
    """validate that num is a 0 or positive integer"""

    if type(value) is not str:
        raise TypeError("value passed to validate_not_neg must be string")
    if type(num) is not int:
        raise TypeError(f"{value} must be an integer")
    if num < 0:
        raise ValueError(f"{value} must be >= 0")
