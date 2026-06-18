"""
This module provides a basic implementation of a singly linked list.
It includes common operations such as append, prepend, delete, and reverse.
"""

class Node:
    """
    A class representing a node in a singly linked list.
    """
    def __init__(self, data):
        """
        Initialize a new node with data.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Add a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """
        Add a new node with the given data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Delete the first occurrence of a node with the given key (data).
        """
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def reverse(self):
        """
        Reverse the linked list in-place.
        """
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        """
        Print the elements of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

if __name__ == "__main__":
    llist = LinkedList()
    print("Appending 1, 2, 3:")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.display()

    print("Prepending 0:")
    llist.prepend(0)
    llist.display()

    print("Deleting 2:")
    llist.delete(2)
    llist.display()

    print("Reversing the list:")
    llist.reverse()
    llist.display()
