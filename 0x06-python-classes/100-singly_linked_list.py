#!/usr/bin/python3
"""Defines a class Square"""

class Node:
    """
    This class defines a Node for a singly linked list.

    The Node class represents a node in the singly linked list with data and a reference to the next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance with the specified data and optional next_node.

        Args:
            data: The data to be stored in the node.
            next_node: The reference to the next node (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Args:
            value: The new value to set for the data.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Args:
            value: The new value to set for the next_node.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    This class defines a Singly Linked List.

    The SinglyLinkedList class represents a singly linked list, which is a collection of linked nodes.

    Attributes:
        head: The reference to the head node of the linked list.

    Methods:
        sorted_insert: Inserts a new node into the sorted position in the linked list.
        __str__: Converts the linked list to a string representation.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the specified value into the sorted position in the linked list.

        Args:
            value: The value to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string representation.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
