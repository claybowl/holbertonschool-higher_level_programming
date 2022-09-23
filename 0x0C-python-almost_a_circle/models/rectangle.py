#!/usr/bin/python3
"""Module rectangle
Class rectangle module
"""


Base = __import__("models.base").base.Base
integer_validator = __import__("models.base").base.integer_validator
no_neg_validator = __import__("models.base").base.no_neg_validator


class Rectangle(Base):
    """Class for Rectangle inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes class Rectangle"""
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        self.no_neg_validator("x", x)
        self.no_neg_validator("y", y)
        self.__x = x
        self.__y = y

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""

        return self.__width

    @property
    def height(self):
        """Retrieves the height of Rectangle instance"""

        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle instance"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @x.setter
    def x(self, value):
        """Sets the x attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
