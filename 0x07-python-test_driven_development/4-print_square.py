#!/usr/bin/python3
"""
Module print_square
Prints square with character #
"""


def print_square(size):
    """
    Size is length and width of square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
