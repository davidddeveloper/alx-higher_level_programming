#!/usr/bin/python3
"""square.py

This module contain classes and method related to square

classes it defined:
    - Square: Represents a square

"""
import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square

    Args:
        - size: size of the square
        - x: x position of the square
        - y: y position of the square

    Attributes:
        Inherits of rectangle

    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Represents the size of the square

        Args:
            - value: integer representing the width

        Raises:
            - TypeError: width must be an integer
            - ValueError: width must be > 0

        """

        self.width = value
        self.height = value
        self.__size = self.width

    def update(self, *args, **kwargs):
        try:
            if args.__len__() != 0:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                for key, value in kwargs.items():
                    if key == "size":
                        self.size = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value
                    if key == "id":
                        self.id = value
        except IndexError:
            pass
        except Exception as e:
            raise (e)

    def to_dictionary(self):
        """Represents the dictionary representation of the rectangle

        Returns:
            the dictionary representation

        """

        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
        }

    def __str__(self):
        return "[{0}] ({1}) {3}/{2} - {4}".format(self.__class__.__name__, self.id, self.y, self.x, self.width)
