#!/usr/bin/env python3

"""
File: LinkedList.py
Author: Cesar Neri <neri102xD@gmail.com>
Date: 04/30/2019

Custom implementation of LinkedList
"""

from Node import Node

#Linked List
class LinkedList():
    """
    LinkedList Class
    Attributes: 
            -SIZE of list
            -HEAD pointer
            -TAIL pointer
    Description: Defines a single direction linked list
    """

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def size(self):
        return self.__size

    def isEmpty(self):
        """
        TRUE is list is empty
        """
        return (self.__size < 1)

    def getFirst(self):
        """
        If the list is not empty, returns the element stored at the beginning of the list
        exception is raised otherwise
        Runtime: O(1)
        """
        if self.isEmpty():
            raise IndexError("Empty Linked List")

        return self.__head.data

    def getLast(self):
        """
        If the list is not empty, returns the element stored at the end of the list
        exception is raised otherwise
        Runtime: O(1)
        """
        if self.isEmpty():
            raise IndexError("Empty Linked List")

        return self.__tail.data

    def get(self, index):
        """
        If the list is not empty, returns the element stored at the specified INDEX
        exception is raised if the list is empty, or INDEX is not between 1 and list SIZE 
        Runtime: O(N)
        """
        if self.isEmpty():
            raise Error("Empty Linked List")

        if (index < 0 or index >= self.size):
            raise IndexError("Invalid index.")

        currentNode = self.__head
        for i in range(index):             
            currentNode = currentNode.nextNode

        return currentNode.data

    def addFirst(self, data):
        """
        New element DATA is added to the front of the list, SIZE of list increases
        Runtime: O(1)
        """
        newNode = Node(data, self.__head)
        
        if self.isEmpty():  #Tail == Head
            self.__tail =  self.__head = newNode
        else:
            self.__head = newNode

        self.__size += 1

    def addLast(self, data):
        """
        New element DATA is added to the back of the list, SIZE of list increases
        Runtime: O(1)
        """
        newNode = Node(data)

        if self.isEmpty():  #Tail == Head
            self.__tail =  self.__head = newNode
        else:
            self.__tail.nextNode = newNode
            self.__tail = newNode

        self.__size += 1

    
    def add(self, index, data):       
        """
        Adds a new specified DATA element to the list at the specified INDEX location, every element 
        after it is moved over one posicion. Specified INDEX must be between 0 and the current size of the list
        Runtime: O(N)
        """
        if (index < 0 or index > self.size):
            raise IndexError("Invalid index.")

        if index == 0:
            self.addFirst(data)

        #Add new element at the end, or list is empty
        elif index == self.size:
            self.addLast(data)

        else:#look ahead
            behindNode = self.__head
            aheadNode = behindNode.nextNode
            for i in range(index-1):             
                behindNode = aheadNode
                aheadNode = behindNode.nextNode

            behindNode.nextNode = Node(data, aheadNode)
            self.__size += 1
        

    def set(self, index, data):
        """
        If the list is not empty, sets the element at the specified INDEX equal to DATA
        exception is raised if the list is empty, or INDEX is not between 1 and list SIZE 
        Runtime: O(N)
        """
        if self.isEmpty():
            raise IndexError("Empty Linked List")

        if (index < 0 or index >= self.size):
            raise IndexError("Invalid index.")

        currentNode = self.__head
        for i in range(index):             
            currentNode = currentNode.nextNode

        currentNode.data = data

    def removeFirst(self):
        """
        If the list is not empty, removes and returns the first element in the list. 
        Exception is raised otherwise
        Runtime: O(1)
        """
        if self.isEmpty():
            raise IndexError("Cannot remove out an element from an empty Linked List")

        else:

            first = self.__head.data
            
            if (self.size == 1):
                self.__tail =  self.__head = None

            else:
                self.__head =  self.__head.nextNode

            self.__size -= 1
            return first

    def removeLast(self):
        """
        If the list is not empty, removes and returns the last element in the list. 
        Exception is raised otherwise
        Runtime: O(N)
        """ 
        if self.isEmpty():
            raise IndexError("Cannot remove out an element from an empty Linked List")

        last = self.__tail.data

        if (self.size == 1):
                self.__tail =  self.__head = None

        else:

            currentNode = self.__head
            while currentNode.nextNode != self.__tail:  #Look ahead search until tail is found
                currentNode = currentNode.nextNode

            currentNode.nextNode = None
            self.__tail = currentNode

        self.__size -= 1

        return last

    def remove(self, index):
        """
        Removes and returns the element at the specified INDEX location.
        Exception is raised for INDEX out of bounds
        Runtime: O(N)
        """
        if (index < 0 or index >= self.size):
            raise IndexError("Invalid index.")

        if index == 0:
            self.removeFirst()

        #Add new element at the end, or list is empty
        elif index == self.size - 1:
            self.removeLast()

        else:#look ahead
            currentNode = self.__head
            for i in range(index-1):
                currentNode = currentNode.nextNode

            indexNode = currentNode.nextNode
            currentNode.nextNode = indexNode.nextNode
            self.__size -= 1

            return indexNode.data
 
    def clear(self):
        """
        Removes all of the current elemnts from the list
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        """
        Returns a STRING that contains every element in the list separet by " "
        """
        listStr = ""
        currentNode = self.__head

        while (currentNode != None):
            listStr += str(currentNode.data) + " "
            currentNode = currentNode.nextNode

        return listStr.rstrip()


#Test Main
def main():

    l1 = LinkedList()
    l1.addFirst(5)
    l1.addFirst(1)
    print(l1)


if __name__ == "__main__":
    main()