#!/usr/bin/python3
"""Module rectangle
Class rectangle module
"""


from models.base import Base
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

        if args is not None and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    """print(f"{key}:{value}")"""
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""

        return self.__width

    @property
    def height(self):
        """Retrieves the height of Rectangle instance"""

        return self.__height

    @width.setter
    def width(self, width):
        """Sets the width of a rectangle instance"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        integer_validator("width", width)
        self.__width = width

    @height.setter
    def height(self, height):
        """Sets the height of a Rectangle instance"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """Retrieves the x attribute"""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @x.setter
    def x(self, num):
        """Sets the x attribute"""

        ##if type(value) is not int:
        ##    raise TypeError("x must be an integer")
        ##if value < 0:
        ##    raise ValueError("x must be >= 0")
        no_neg_validator("x", num)
        self.__x = num

    @y.setter
    def y(self, num):
        """Sets the y attribute"""

        ## if type(value) is not int:
        ##    raise TypeError("y must be an integer")
        ##if value < 0:
        ##    raise ValueError("y must be >= 0")
        no_neg_validator("y", num)
        self.__y = num

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
