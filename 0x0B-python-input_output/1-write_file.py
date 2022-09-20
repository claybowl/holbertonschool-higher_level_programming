#!/usr/bin/python3
"""Module 1-write_file
writes a string to a text file and
returns number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to text file and returns number of characters"""

    with open(filename, 'r+') as f:
        return f.write(text)
