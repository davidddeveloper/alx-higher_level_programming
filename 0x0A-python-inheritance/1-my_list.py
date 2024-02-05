#!/usr/bin/python3
"""1-my_list.py

This module contains classes and method related to list

classes contained in it:
    - MyList: share properties from the list object

"""


class MyList(list):
    """Represents a list with additional methods

    """

    def print_sorted(self):
        """Prints a sorted list"""

        new_list = self.copy()
        new_list.sort()
        print(new_list)
