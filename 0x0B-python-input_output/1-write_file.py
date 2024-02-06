#!/usr/bin/python3
"""1-write_file.py

This module provides function for writing to a file

"""


def write_file(filename="", text=""):
    """Reads a text file and prints to stdout

    Args:
        - filename: the name of the file
        - text: the content to write

    """

    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
