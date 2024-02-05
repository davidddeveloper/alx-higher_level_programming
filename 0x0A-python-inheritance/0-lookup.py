#!/usr/bin/python3
"""0-lookup.py

This module contain a function for printing the attributes in an object
the function contain in it:
    - lookup(obj): return a list of attributes contained in obj

"""


def lookup(obj):
    """A function for looking up the attributes in an object
    
    Returns:
        A list containing the attributes

    """
    return dir(obj)
