#!/usr/bin/python3
""" writes a class square"""


class Square:
    """attempt to model a square"""

    def __init__(self, size=0):  # instantiation happens here
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):  # method to retrieve squares size
        return self.__size

    @size.setter
    def size(self, value):  # method to set/change squares size
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
