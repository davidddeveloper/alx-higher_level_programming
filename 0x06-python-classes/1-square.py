#!/usr/bin/python3
"""1-square.py

This module define functionality for creating a square using oop

It contains the following classes:
    - Square: Represent the method for creating a square

"""


class Square:
    """Represent the square

    Args:
        size: size of square

    Attributes:
        __size: size of square

    """

    def __init__(self, size):
        self.__size = size
