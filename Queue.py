#!/usr/bin/env python3

"""
File: Queue.py
Author: Cesar Neri <neri102xD@gmail.com>
Date: 05/07/2019

Custom implementation of Queue using my custom LinkedList.
Queue makes use only of LinkedList methods that would guarante 
an O(1) runtime for all of the Queue basic methods.
"""

from LinkedList import LinkedList

class Queue(object):

    def __init__(self):
        self.__Llist = LinkedList()

    def __len__(self):
        return self.__Llist.__len__()

    def __str__(self):
        """
        Returns a STRING that contains every element in the Queue.
        Top of the Queue indicated by "->" character.
        """
        return "-> " + self.__Llist.__str__()


    def isEmpty(self):
        """
        True if current Queue is empty, False otherwise.
        """
        return self.__Llist.isEmpty()


    def add(self, data):
        """
        Inserts a new element DATA at the end of the Queue.
        Runtime: O(1)
        """
        self.__Llist.addLast(data)

    def peek(self):
        """
        Returns the element at the top of the Queue withouth
        removing it.
        Runtime: O(1)
        """
        dataPeeked = None

        try:
            dataPeeked = self.__Llist.getFirst()
        except IndexError: #as e:
            print("Cannot peek on an empty Queue")

        return dataPeeked
    
    def poll(self):
        """
        Removes and returns the element at the top of the Queue.
        Runtime: O(1)
        """
        dataPopped = None

        try:
            dataPopped = self.__Llist.removeFirst()
        except IndexError: #as e:
            print("Cannot pop from an empty Queue")

        return dataPopped


def main():

    #Dummy main that test basic functionality
 
    q1 = Queue()

    print("Queue created") 
    print("Size of queue:", len(q1), "\n")

    print("Add 3")
    q1.add(3)
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    print("Add 2")
    q1.add(2)
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    print("Add 1")
    q1.add(1)
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    print("Peek:", q1.peek())
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    print("Poll:", q1.poll())
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    print("Poll:", q1.poll())
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    print("Poll:", q1.poll())
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    #Test empty list exceptions handling

    print("Peek:", q1.peek())
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

    print("Poll:", q1.poll())
    print("Queue:", q1)
    print("Size of queue:", len(q1), "\n")

if __name__ == "__main__":
    main()
