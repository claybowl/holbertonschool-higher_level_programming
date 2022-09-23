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
        integer_validator("width", width)
        integer_validator("height", height)
        self.__width = width
        self.__height = height
        no_neg_validator("x", x)
        no_neg_validator("y", y)
        self.__x = x
        self.__y = y

    def __str__(self):
        """Returns an informal and nicely printable string"""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def display(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""

        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """update rectangle class"""

        newargs = [self.id, self.__width, self.__height, self.__x, self.__y]
        if len(args) > 0:
            for i in range(len(args)):
                newargs[i] = args[i]
        else:
            for i in kwargs:
                if i == "id":
                    newargs[0] = kwargs[i]
                if i == "width":
                    newargs[1] = kwargs[i]
                if i == "height":
                    newargs[2] = kwargs[i]
                if i == "x":
                    newargs[3] = kwargs[i]
                if i == "y":
                    newargs[4] = kwargs[i]
        self.__init__(
            newargs[1], newargs[2], newargs[3], newargs[4], newargs[0])

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

        integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""

        integer_validator("height", value)
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

        no_neg_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""

        no_neg_validator("y", value)
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def to_dictionary(self):
        """return dictionary"""

        return {'id': self.id, 'width': self.width, 'height':
                self.height, 'x': self.x, 'y': self.y}
