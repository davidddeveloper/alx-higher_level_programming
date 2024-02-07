#!/usr/bin/python3
"""6-load_from_json_file.py

This module contains a function
for converting a json string in a file to python object

"""
import json


def load_from_json_file(filename):
    """converts a json string in a file to python object"""

    with open(filename,) as f:
        data = json.load(f)
        return data
