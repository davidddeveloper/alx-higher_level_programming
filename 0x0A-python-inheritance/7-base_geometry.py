#!/usr/bin/python3
"""7-base_geometry.py

This module contain classes and methods related to geometry

classes it contain:
    - BaseGeometry: defines a geometry
"""


class BaseGeometry:
    """Represents a Geometry"""

    def area(self):
        """Calculates the area of a geometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an integer

        Args:
            - name: describe the content of the value
            - value: an integer value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
