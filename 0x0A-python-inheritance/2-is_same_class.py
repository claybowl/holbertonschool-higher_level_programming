#!/usr/bin/python3
"""Module 2-is_same_class
Function that returns true if object is exactly
an instance of the specified class. Otherwise False
"""


def is_same_class(obj, a_class):
    """Identifies class instance"""

    if isinstance(obj, a_class):
        print(True)
	if not isinstance(obj, a_class):
		print(False)
