#!/usr/bin/python3
"""Writing a class that defines a
rectangle by width and height
"""


class Rectangle:
    """Rectangle class defined by width and height.
    """

    def __init__(self, width=0, height=0):
        """Initialize weight and height attributes
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of Rectangle instance
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle instance
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value