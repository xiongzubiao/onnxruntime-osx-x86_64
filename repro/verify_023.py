"""
Module for verifying singly linked list implementation.
This module provides a Node and a SinglyLinkedList class with common operations.
"""

class Node:
    """
    A class representing a node in a singly linked list.
    """
    def __init__(self, data):
        """
        Initialize a node with data.
        """
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    A class representing a singly linked list.
    """
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def append(self, data):
        """
        Append a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Prepend a new node with the given data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Delete the first occurrence of a node with the given data (key).
        """
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def reverse(self):
        """
        Reverse the singly linked list in-place.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        """
        Return a string representation of the list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

if __name__ == "__main__":
    # Demonstration of SinglyLinkedList functionality
    llist = SinglyLinkedList()
    
    print("Appending 1, 2, 3:")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print(llist.display())

    print("\nPrepending 0:")
    llist.prepend(0)
    print(llist.display())

    print("\nDeleting 2:")
    llist.delete(2)
    print(llist.display())

    print("\nReversing list:")
    llist.reverse()
    print(llist.display())
