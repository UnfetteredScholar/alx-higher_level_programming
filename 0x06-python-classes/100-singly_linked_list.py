#!/usr/bin/python3
"""Defines the Classes Node and SinglyLinkedList"""


class Node:
    """Defines a Node object

    Attributes:
        data (int): the data stored by the node
        next_node (Node): the next node
    """
    def __init__(self, data, next_node=None):
        """Initializes a Node object

        Args:
            data (int): the data stored by the node
            next_node (Node): the next node
        """

        if type(data) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = data

        if next_node is None or type(next_node) is Node:
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """Gets or Sets the data attribute

        Raises:
           TypeError: if data is not an int
        """
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = data

    @property
    def next_node(self):
        """Gets or Sets the next_node attribute

        Raises:
            TypeError: if not a Node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """Defines a SinglyLinkedList object

    Attributes:
        head (Node): the head of the list
    """

    def __init__(self):
        """Initialized SinglyLinkedList object"""
        self.__head = None

    def __str__(self):
        """String representation of SinglyLinkedList"""
        curr = self.__head
        res = ""

        while curr is not None:
            res += f'{curr.data}'
            if curr.next_node is not None:
                res += '\n'
            curr = curr.next_node
        return res

    def sorted_insert(self, value):
        """Adds a new node to the list in a sorted position

        Args:
            value (int): the value to be inserted
        """
        new = Node(value)

        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            curr = self.__head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            new.next_node = curr.next_node
            curr.next_node = new
