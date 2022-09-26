#!/usr/bin/python3
"""module base_test
unittest for doc_sting
"""


import inspect
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pep8
import json
import os
import pycodestyle


class Test_Base(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_pep8_base(self):
        """Test that models/base.py is pep8 compliant."""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """Test that tests/test_models/test_base.py is pep8 compliant"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""

        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""

        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""

        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)

    def test_to_json_string(self):
        """Tests regular to json string"""

        Base._Base__nb_objects = 0
        d1 = {"id": 98, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_empty_to_json_string(self):
        """Test for passing empty list/ None"""

        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_fjs_None(self):
        """Tests from_json_string with an empty string"""

        self.assertEqual([], Base.from_json_string(None))

    def test_None_to_json_String(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests regular from_json_string"""

        json_str = '[{"id": 98, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 98, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

        

if __name__ == '__main__':
    unittest.main()