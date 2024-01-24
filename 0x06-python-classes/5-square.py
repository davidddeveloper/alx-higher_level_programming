#!/usr/bin/python3
"""4-square.py

This module provide functionality related to squares

classed define in module:
    - Square: Represents a square and provides method for calculations

"""


class Square:
    """Represents a square and provides method for calculations

    Args:
        - size: size of square

    Attributes:
        - __size: size of square

    Methods:
        - my_print(): prints in stdout the square with the character #

    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square.

        Args:
            - value (int): The new size of each side of the square

        Returns:
            int: the size of each side of the square.

        """

        return self.__size

    @size.setter
    def size(self, value):
        if value == f"{value}":
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Represent the area of a square

        Returns:
            int: the area of the square

        """

        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #

        Returns:
            None
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
