#!/usr/bin/python3
"""7-add_item.py

This module provides function for adding
all arguments to a python list and saves them to a file

"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """adds all arguments to a Python list,
    and then save them to a file"""

    args_list = sys.argv
    args_list = args_list[1:]
    filename = "add_item.json"

    # Converting to json and saving it to a file
    save_to_json_file(args_list, filename)

    # Reads a json string from a file
    # and converts to python object
    load_from_json_file(filename)


main()
