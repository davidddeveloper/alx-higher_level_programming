#!/usr/bin/python3
"""2-square.py

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

    """

    def __init__(self, size=0):
        if size == f"{size}":
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
