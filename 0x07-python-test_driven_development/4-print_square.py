#!/usr/bin/python3
"""4-print_square.py

This module contain a function for printing a square with the #

function defined in square:
    print_square(size): prints a square with the #

"""


def print_square(size):
    """prints a square with the #

    Args:
        - size: size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("{}".format("#" * size))
