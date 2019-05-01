#!/usr/bin/env python3

"""
File: Node.py
Author: Cesar Neri <neri102xD@gmail.com>
Date: 04/29/2019

Custom implementation of List Node
"""

#Node
class Node():
    """
    Node Class
    Attributes: DATA and NEXTNODE
    Description: Defiones the nodes in a linked list
    """

    def __init__(self, data=None, nextN=None):

        self.__nextNode = nextN 
        self.__data = data

    @property
    def nextNode(self):
        return self.__nextNode

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @nextNode.setter
    def nextNode(self, nxtNode):
        if isinstance(nxtNode, Node) or (nxtNode == None) :
            self.__nextNode = nxtNode
        else:
            raise TypeError("Node must point to an object of type Node")

    def __str__(self):
        return "Node with data: " + str(self.__data)