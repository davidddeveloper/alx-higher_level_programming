#!/usr/bin/python3
"""100-singly_linked_list.py

This module provides functionality related to the creation of singly linked list

classes it define:
    Node: defines a node of a singly linked list
    SinglyLinkedList: defines a singly linked list

"""


class Node:
    """Represent a node of a singly linked list

    Args:
        - data (int): integer to insert in the node
        - next_node: a node

    Attributes:
        - __data (int): integer to insert in the node
        - __next_node: a node

    """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node


    @property
    def data(self):
        """Represent a property for accessing and modifying the data

        Args:
            - node: a object or none

        Raises:
            TypeError: if node is not an object or node is not None

        """
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, node):
        if node is not None or type(node) is not Node:
            raise TypeError("next_node must be a Node object") from None
        self.__next_node = node


class SinglyLinkedList:
    """Represent a singlylinkedlist

    Attributes:
        - __head: a Node object representing the start of the singly linked list
        - __current: a Node object for traversing the list
        - new_node: a Node object

    Methods:
        sorted_insert(value: int) -> None: inserts a new Node

    """

    def __init__(self):
        print("Initializing...")
        self.__head = None
        self.current = None
        self.new_node = Node(0, None)

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list

        Args:
            - value (int): the integer for the node

        Returns:
            None
        """
        self.new_node.data = value

        if self.__head is None:
            self.__head = self.new_node
            return

        self.current = self.__head

        while (self.current != None):
            self.current = self.current.next_node

        self.current = self.new_node
        print("data of head", self.__head.data)

    def __repr__(self):
        """String reprsentation of the list

        Returns:
            (str): string representation of the instance
        """
        print("value of head in repr", self.__head.data)

        while (self.__head != None):
            print("{}".format(self.__head.data))
            self.__head = self.__head.next_node

        return f""
