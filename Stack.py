#!/usr/bin/env python3

"""
File: Stack.py
Author: Cesar Neri <neri102xD@gmail.com>
Date: 05/02/2019

Custom implementation of Stack using my custom LinkedList
Stack makes use only of LinkedList methods that would guarante 
an O(1) runtime for all of the Stack basic methods.
"""

from LinkedList import LinkedList

class Stack(object):

    def __init__(self):
        self.__Llist = LinkedList()

    def __len__(self):
        return self.__Llist.__len__()

    def __str__(self):
        """
        Returns a STRING that contains every element in the Stack.
        Top of the Stack indicated by "->" character.
        """
        return "-> " + self.__Llist.__str__()


    def isEmpty(self):
        """
        True if current Stack is empty, False otherwise.
        """
        return self.__Llist.isEmpty()


    def push(self, data):
        """
        Inserts a new element DATA at the top of the Stack.
        Runtime: O(1)
        """
        self.__Llist.addFirst(data)

    def peek(self):
        """
        Returns the element at the top of the Stack withouth .
        removing it.
        Runtime: O(1)
        """
        dataPeeked = None

        try:
            dataPeeked = self.__Llist.getFirst()
        except IndexError: #as e:
            print("Cannot peek on an empty Stack")

        return dataPeeked
    
    def pop(self):
        """
        Removes and returns the element at the top of the Stack.
        Runtime: O(1)
        """
        dataPopped = None

        try:
            dataPopped = self.__Llist.removeFirst()
        except IndexError: #as e:
            print("Cannot pop from an empty Stack")

        return dataPopped


def main():

    #Dummy main that test basic functionality

    print("Stack created") 
    s1 = Stack()

    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Push 3")
    s1.push(3)
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Push 2")
    s1.push(2)
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Push 1")
    s1.push(1)
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Peek:", s1.peek())
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Pop:", s1.pop())
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Pop:", s1.pop())
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Pop:", s1.pop())
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    #Test empty list exceptions handling

    print("Peek:", s1.peek())
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

    print("Pop:", s1.pop())
    print("Stack:", s1)
    print("Size of stack:", len(s1), "\n")

if __name__ == "__main__":
    main()
