"""base.py

This module contain classes and method related to geometry shapes

classes it defined:
    - Base: Represent the base of all other classes

"""


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
