#!/usr/bin/python3
"""Module 1-my_list
Writes a class 'MyList' that inherits from
class 'list'
"""


class MyList(list):
    """List with attributes of parent class"""

    def __init__(self):
        """Initiating list"""
        super().__init__(self)

    def print_sorted(self):
        """Prints list in ascending order"""

        my_list = self[:]
        my_list.sort()
        print("{}".format(my_list))
