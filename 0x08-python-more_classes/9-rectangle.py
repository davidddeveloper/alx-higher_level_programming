#!/usr/bin/python3
"""9-rectangle.py
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

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self._symbol = "#"
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def print_symbol(self, value):
        self._symbol = value

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
            raise ValueError("height must be >= 0") from None
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.width == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_of_rect_1 = Rectangle.area(rect_1)
        area_of_rect_2 = Rectangle.area(rect_2)

        if area_of_rect_1 > area_of_rect_2:
            return rect_1
        if area_of_rect_2 == area_of_rect_1:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __str__(self):
        """A more informal and nicely printed representation of the string

        """

        rect = ""
        if self.width == 0 or self.height == 0:
            return rect

        for i in range(self.height):
            rect += self._symbol * self.width

            if i != (self.height - 1):
                rect += "\n"

        return (rect)

    def __repr__(self):
        """An official representation of the string

        """

        return f"{self.__class__.__name__}({self.width}, {self.height})"
