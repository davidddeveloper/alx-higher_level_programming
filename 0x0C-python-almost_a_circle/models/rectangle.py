#!/usr/bin/python3
"""rectangle.py

This module contain classes and method related to rectangle

classes it defined:
    - Rectangle: Represents a rectangle

"""
import json
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle

    Args:
        - width: width of the rectangle
        - height: height of the rectangle
        - id: a unique number associated with every instance

    Attributes:
        - width: width of the rectangle
        - height: height of the rectangle
        - id: a unique number associated with every instance

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Represents the width of the rectangle

        Args:
            - value: integer representing the width

        Raises:
            - TypeError: width must be an integer
            - ValueError: width must be > 0

        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Represents the height of the rectangle

        Args:
            - value: integer representing the height

        Raises:
            - TypeError: height must be an integer
            - ValueError: height must be > 0

        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """Represents the x position of the rectangle

        Args:
            - value: integer value

        Raises:
            - TypeError: x must be an integer
            - ValueError: x must be >= 0

        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """Represents the y position of the rectangle

        Args:
            - value: integer value

        Raises:
            - TypeError: y must be an integer
            - ValueError: y must be >= 0

        """

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints out the shape of the rectangle using #"""

        for i in range(self.__y):
            print()
        for row in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            print("{}".format(self.__width * '#'))

    def update(self, *args, **kwargs):
        """Updates an object"""

        try:
            if args.__len__() != 0:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            else:
                for key, value in kwargs.items():
                    if key == "height":
                        self.height = value
                    if key == "width":
                        self.width = value
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
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
        }

    def __str__(self):
        return "[{0}] ({1}) {5}/{4} - {2}/{3}".format(self.__class__.__name__,
                self.id, self.__width, self.__height, self.__y, self.__x)
