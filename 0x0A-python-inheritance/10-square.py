#!/usr/bin/python3
"""10-square.py

This module contains classes and methods related to square

classes contained in it:
    - Square: Represent a square

"""


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def are():
        """Calculates the area of the square

        Returns:
            the area of the square -> int

        """

        return self.__size ** 2
