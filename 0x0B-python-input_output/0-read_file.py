#!/usr/bin/python3
"""0-read_file.py

This module provides function for reading a file

"""


def read_file(filename=""):
    """Reads a text file and prints to stdout

    Args:
        - filename: the name of the file

    """

    with open(filename) as f:
        print(f.read())
