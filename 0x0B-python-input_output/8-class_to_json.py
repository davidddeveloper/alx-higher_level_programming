#!/usr/bin/python3
"""8-class_to_json.py

This module provides a function for converting
a custom class to json object

"""


def class_to_json(obj):
    """Converts a custom object to json

    Args:
        - obj: the custom object

    returns:
        - the json representation
    """

    return obj.__dict__
