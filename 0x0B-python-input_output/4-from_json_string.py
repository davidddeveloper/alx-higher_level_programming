#!/usr/bin/python3
"""3-to_json_string.py

This module contains a function
for converting JSON to object

"""
import json


def from_json_string(my_str):
    """Converts JSON string to an object"""

    return json.loads(my_str)
