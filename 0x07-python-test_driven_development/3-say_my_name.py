#!/usr/bin/python3
"""3-say_my_name.py

This module contains function related to printing a users name

functions it contained:
    - def say_my_name(first_name, last_name="") -> None

"""


def say_my_name(first_name, last_name=""):
    if type(first_name) != str:
        raise TypeError("first_name must be a string or last_name must be a string")
    if type(last_name) != str:
        raise TypeError("first_name must be a string or last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
