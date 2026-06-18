"""
Singly Linked List implementation for verification.
This module provides a basic singly linked list with common operations.
"""

class Node:
    """
    Represents a single node in a linked list.
    """
    def __init__(self, data):
        """
        Initialize a node with data and a pointer to the next node.
        """
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    A class to represent and manipulate a singly linked list.
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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Add a new node with the given data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Delete the first occurrence of a node containing the specified key.
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
        Reverse the linked list in place.
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
        Print the elements of the list in order.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")

if __name__ == "__main__":
    # Demonstration of SinglyLinkedList functionality
    print("Creating a new Singly Linked List...")
    llist = SinglyLinkedList()

    print("\nAppending 10, 20, 30:")
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.display()

    print("\nPrepending 5:")
    llist.prepend(5)
    llist.display()

    print("\nDeleting 20:")
    llist.delete(20)
    llist.display()

    print("\nReversing the list:")
    llist.reverse()
    llist.display()
