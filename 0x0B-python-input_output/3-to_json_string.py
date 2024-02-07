#!/usr/bin/python3
"""3-to_json_string.py

This module contains a function
for converting an object to JSON

"""
import json


def to_json_string(my_obj):
    """Converts an object to JSON"""

    return json.dumps(my_obj)
