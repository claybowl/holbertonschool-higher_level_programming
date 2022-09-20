#!/usr/bin/python3
"""Module 9-student
Writes a class 'Student' that defines students by first_name,
last_name, age"""


class Student:
    """Creates a Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes student attributes"""

        pass

    def to_json(self):
        """retrieves dictionary representation of student instance"""

        return self.__dict__
