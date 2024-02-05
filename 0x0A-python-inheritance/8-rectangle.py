#!/usr/bin/python3
"""8-rectangle.py
This module contain classes and methods related to rectangle

classes it contained:
    - Rectangle: Represents a rectangle

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle

    Args:
        - width: width of the rectangle
        - height: height of the rectangle

    Attributes:
        - __width: width of the rectangle
        - __height: height of the rectangle

    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
