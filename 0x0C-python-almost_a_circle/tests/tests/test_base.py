#!/usr/bin/python3
"""
Test for Base Class
"""
import inspect
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pycodestyle
import pep8
import json
import os


class TestBaseClass(unittest.TestCase):
    """
    Test Base Class
    """

    def test_pep8_base(self):
        """
        Test that models/base.py is pep8 compliant.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()
