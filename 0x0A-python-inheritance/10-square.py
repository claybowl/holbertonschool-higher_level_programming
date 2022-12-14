#!/usr/bin/python3
"""
Creates class Square which is 
sub-class of Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initializing size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns string of super class"""

        return super().__str__()

    def area(self):
        """area of Square"""

        return self.__size ** 2
