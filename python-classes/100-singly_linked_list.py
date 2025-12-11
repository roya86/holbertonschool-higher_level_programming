#!/usr/bin/python3
"""Define classes for a singly linked list."""


class Node:
    """Represent a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize an empty list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node in sorted ascending order."""
        new = Node(value)

        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new.next_node = current.next_node
        current.next_node = new
