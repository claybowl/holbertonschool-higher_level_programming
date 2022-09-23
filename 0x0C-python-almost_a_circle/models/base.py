#!/usr/bin/python3
"""Module base.py
Base class for for all modules
"""


import json
import os
import csv


class Base:
    """base class for geometric objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON string to file"""

        with open(cls.__name__ + ".json", 'w') as jsonfile:
            emptylist = []
            if list_objs is not None and len(list_objs) > 0:
                for i in list_objs:
                    emptylist.append(i.to_dictionary())
            jsonfile.write(cls.to_json_string(emptylist))

    @classmethod
    def create(cls, **dictionary):
        """Creates and returns an object instance defined by **dictionary kwargs
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of object instances created fromjson file <class>.json"""

        jsonfilename = cls.__name__ + ".json"
        try:
            with open(jsonfilename, "r") as jsonfile:
                jsonlist = cls.from_json_string(jsonfile.read())
            objectlist = []
            for object in jsonlist:
                objectlist.append(cls.create(**object))
            return objectlist
        except:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turns list of dictionaries into JSON string"""

        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation
        """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)
