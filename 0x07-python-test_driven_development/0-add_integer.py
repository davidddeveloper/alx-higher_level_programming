#!/usr/bin/python3
"""0-add_integer.py
    __test__ = {"external", "tests/0-add_integer.txt"}
"""


def add_integer(a, b=98):
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if a is None:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
