#!/usr/bin/python3
"""8-class_to_json.py

This module provides a function for converting
a custom class to json object

"""
import json


def class_to_json(obj):
    """Converts a custom object to json

    Args:
        - obj: the custom object

    returns:
        - the json representation
    """

    json_obj = json.dumps(obj, default=lambda o: o.__dict__)
    return json.loads(json_obj)
