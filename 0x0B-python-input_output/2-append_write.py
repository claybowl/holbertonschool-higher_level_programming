#!/usr/bin/python3
"""Module 2-append_write
Appends a string at the end of a text file
Returns number of characters added
"""


def append_write(filename="", text=""):
    """appends string at end of text file and returns number of characters"""

    with open(filename, 'a+') as f:
        return f.write(text)
