#!/usr/bin/python3
"""Module 1-my_list
Writes a class 'MyList' that inherits from
class 'list'
"""


class MyList(list):
    """List with attributes of parent class"""

    def print_sorted(self):
        """Prints list in ascending order"""

        my_list = self[:]
        my_list.sort()
        print("{}".format(self))
