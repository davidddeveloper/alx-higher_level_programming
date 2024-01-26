#!/usr/bin/python3
"""100-singly_linked_list.py

This module provides functionality related to singly linked list

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
        #if node is not None or isinstance(node, Node):
            #raise TypeError("next_node must be a Node object") from None
        self.__next_node = node


class SinglyLinkedList:
    """Represent a singlylinkedlist

    Attributes:
        - __head: a Node representing the start of the singly linked list
        - __current: a Node object for traversing the list
        - new_node: a Node object

    Methods:
        sorted_insert(value: int) -> None: inserts a new Node

    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list

        Args:
            - value (int): the integer for the node

        Returns:
            None
        """

        self._new_node = Node(value)

        if self.__head is None or value <= self.__head.data:
            self._new_node.next_node = self.__head
            self.__head = self._new_node

        else:
            current = self.__head

            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node

            self._new_node.next_node = current.next_node
            current.next_node = self._new_node

    @property
    def print_list(self):
        current = self.__head
        while current is not None:
            print(current.data)
            current = current.next_node

    def __repr__(self):
        """String reprsentation of the list

        Returns:
            (str): string representation of the instance

        """

        current = self.__head
        while current is not None:
            print(current.data)
            current = current.next_node

        return f""
