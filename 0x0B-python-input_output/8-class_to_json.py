#!/usr/bin/python3
"""8-class_to_json.py

This module provides a function for converting
a custome class to json object

"""
import json


def class_to_json(obj):
    """Converts a custom object to json

    Args:
        - obj: the custom object

    returns:
        - the json representation
    """

    return json.dumps(obj, default=lambda o: o.__dict__)
