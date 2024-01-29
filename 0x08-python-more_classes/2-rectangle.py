#!/usr/bin/python3
"""1-rectangle.py
    This module containes function classes related to Rectangle

    classes define in it:
        - Rectangle: provides attributes for creating a rectangle

"""


class Rectangle:
    """provides attributes for creating a rectangle

    Args:
        - width: width of rectangle
        - height: height of rectangle

    Attributes:
        - width: width of rectangle
        - height: height of rectangle
        - __width: width of rectangle
        - __height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """the width of the rectangle

            Args:
                - value: value of width
        """

        if type(value) != int:
            raise TypeError("width must be an integer") from None
        if value < 0:
            raise ValueError("width must be >= 0") from None
        self.__width = value

    @height.setter
    def height(self, value):
        """represent the height of the rectangle

            Args:
                - value: value of width

        """
        if type(value) != int:
            raise TypeError("height must be an integer") from None
        if value < 0:
            raise ValueError("width must be >= 0") from None
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.width == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
