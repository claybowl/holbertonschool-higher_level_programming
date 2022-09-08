#!/usr/bin/python3

from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
"""Asyncio"""

class Square:
    """ class for defined Square """
    def __init__(self, size=0):
            """__init__ defined"""
	    if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
