#!/usr/bin/python3
"""base.py

This module contain classes and method related to geometry shapes

classes it defined:
    - Base: Represent the base of all other classes

"""
import json


class Base:
    """Represent the base of all other classes

    Args:
        - id: a unique number associated with every instance

    Attributes:
        - id: a unique number associated with every instance

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Represents a json string

        Args:
            - list_dictionaries: a list of dictionaries

        Returns:
            - JSON string representation of list_dictionaries
            - otherwise if list_dictionaries is None or empty,
            return the string: "[]"

        """

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list of object to a file

        Args:
            - list_objs: list of objects

        """

        list_of_dict = []  # list of dictionary representation of obj
        for obj in list_objs:
            # get dictionary representation of the obj
            list_of_dict.append(obj.to_dictionary())

        # converts to json string
        json_list_of_dict = cls.to_json_string(list_of_dict)

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='UTF-8') as f:
            # save json_list_of_dict to a file with the class name
            json.dump(json_list_of_dict, f)

    def from_json_string(json_string):
        """converts from JSON string to python list

        Args:
            - json_string: a string representing a list of dictionaries

        Returns:
            - the list represented by json_string
            - otherwise an empty list
        """

        if json_string is None:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates and instance

        Args:
            - dictionary: a kwargs containing
            all the values for the instance attributes

        """

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 10)

        else:  # it is a square
            dummy_instance = cls(10)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """loads the JSON string representation of list of object from a file
        to a python list


        """

        filename = cls.__name__ + ".json"
        with open(filename, 'r', encoding="utf-8") as f:
            # load json list of dict from a file with the class name
            if (f.read() == ""):  # file is empty
                return []

            f.seek(0)
            json_list_of_dict = json.load(f)

        list_of_dict = cls.from_json_string(json_list_of_dict)
        list_of_obj = []
        for dictionary in list_of_dict:
            # creates objects and save to a list
            list_of_obj.append(cls.create(**dictionary))

        return list_of_obj
