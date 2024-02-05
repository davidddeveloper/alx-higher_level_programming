#!/usr/bin/python3
"""3-is_kind_of_class.py

This module contains a function for checking if an object
is an instance of a class that inherited from the specified class

the function it contain:
    - is_kind_of_class(obj, a_class) -> bool: checks if an object is an
    instance of a specified class

"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of a class
    that inherited form the specified class

    Returns:
       - True: if obj is an instance of a_class
       that inherited form the specified class
       - False: otherwise

    """

    return issubclass(type(obj), a_class)
