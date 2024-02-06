#!/usr/bin/python3
"""0-read_file.py

This module provides function for appending to a file

"""


def append_write(filename="", text=""):
    """Appends to a text file

    Args:
        - filename: the name of the file
        - text: content to be written

    """

    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
