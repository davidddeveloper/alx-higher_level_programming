"""2-is_same_class.py

This module contains a function for checking if an object
is an instance of a specified class

the function it contain:
    - is_same_class(obj, a_class) -> bool: checks if an object is an
    instance of a specified class

"""


def is_same_class(obj, a_class):
    """checks if an object is aninstance of a specified class
    
    Returns:
       - True: if obj is an instance of a_class
       - False: otherwise

    """

    return isinstance(obj, a_class)
