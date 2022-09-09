#!/usr/bin/python3
""" writes a class square"""


class Square:
    """attempt to model a square"""

    def __init__(self, size=0):  # instantiation happens here
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
