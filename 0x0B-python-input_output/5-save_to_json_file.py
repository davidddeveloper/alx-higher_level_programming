#!/usr/bin/python3
"""5-save_to_json_file.py

This module contains a function
for writing an object to a json file

"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a json file"""

    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
