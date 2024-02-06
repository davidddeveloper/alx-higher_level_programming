#!/usr/bin/python3
"""10-square.py

This module contains classes and methods related to square

classes contained in it:
    - Square: Represent a square

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square

    Args:
        - size: the size of the square

    Attributes:
        - __size: the size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: is size is less than or equal to zero

    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def are():
        """Calculates the area of the square

        Returns:
            the area of the square -> int

        """

        return self.__size ** 2
