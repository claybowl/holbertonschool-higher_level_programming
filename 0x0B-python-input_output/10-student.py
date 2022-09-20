#!/usr/bin/python3
"""Module 9-student
Writes a class 'Student' that defines students by first_name,
last_name, age"""


class Student:
    """Creates a Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes student attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of student instance"""

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict

        return self.__dict__.copy()
