#!/usr/bin/python3

"""represent a square"""

class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """This method initializes the square
	Size is the length of any side
	Size will be a private attribute"""
        if not isinstance(size, int):
	    raise TypeError("size must be an integer")
        self.__size = size
	if size < 0:
            raise ValueError("size must be >= 0")
