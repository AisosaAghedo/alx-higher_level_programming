#!/usr/bin/python3
"""This module contains a class that defines a Node.
In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
"""


class Node():
    """Node Class."""

    def __init__(self, data, next_node=None):
        """Initialization of Node Class"""
        
        self.data = data
        self.next_node = next_node

    @property
    def data(self):

        """retrives data"""
        return self.__data

    @data.setter
    def data(self, DataValue):
        """Sets data"""

        if type(DataValue) != int:
            raise TypeError("data must be an integer")
        self.__data = DataValue

    @property
    def next_node(self):
        """gets Node"""
        
        return self.__next_node

    @next_node.setter
    def next_node(self, NodeValue):
        """sets Node"""
        
        if NodeValue is not None and not isinstance(NodeValue, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = NodeValue


class SinglyLinkedList():
    """Class SinglyLinkedList"""
    
    def __init__(self):
        """Initialization of SinglyLinkedList class"""
        
        self.__head = None

    def sorted_insert(self, DataValue):
        """Inserts a node"""
        
        New = Node(DataValue)
        if self.__head is None:
            self.__head = New
            return
        if DataValue < self.__head.data:
            New.next_node = self.__head
            self.__head = New
            return
        temp = self.__head
        while DataValue >= actual.data:
            prev = temp
            if temp.next_node:
                temp = temp.next_node
            else:
                temp.next_node = New
                return
        prev.next_node = New
        New.next_node = temp

    def __str__(self):
        """String"""

        strg = ""
        temp = self.__head
        while temp:
            strg += str(temp.data) + "\n"
            temp = temp.next_node
        return strg[:-1]
