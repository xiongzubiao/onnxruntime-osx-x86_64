"""
Singly Linked List Implementation

This module provides a basic implementation of a singly linked list with
methods for appending, prepending, deleting nodes, and reversing the list.
"""

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Add a new node with data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """Add a new node with data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first node that contains the specified key."""
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr = None

    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def display(self):
        """Print the contents of the list."""
        elems = []
        curr = self.head
        while curr:
            elems.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elems) if elems else "Empty List")

if __name__ == "__main__":
    # Demonstration of the SinglyLinkedList
    llist = SinglyLinkedList()
    
    print("Appending 1, 2, 3:")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.display()

    print("\nPrepending 0:")
    llist.prepend(0)
    llist.display()

    print("\nDeleting 2:")
    llist.delete(2)
    llist.display()

    print("\nReversing the list:")
    llist.reverse()
    llist.display()
