#!/usr/bin/python3
"""Module 0-read_file
Reads file and prints to stdout
"""


def read_file(filename=""):
    """reads file and prints to stdout"""

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
