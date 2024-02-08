#!/usr/bin/python3
"""8-class_to_json.py

This module provides methods for converting
a custom class to json object

"""


class Student:
    """Represents a student class

    Args:
        - first_name: student first name
        - last_name: student last name
        - age: student age

"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts a custom object to json

        Args:
            - obj: the custom object

        returns:
            - the json representation
        """

        return self.__dict__
