"""
Singly Linked List Implementation

This module provides a basic implementation of a singly linked list with
standard operations such as append, prepend, delete, and reverse.
"""

class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, data):
        """Initialize the node with data and set next to None."""
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """Add a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first occurrence of a node with the given data (key)."""
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        """Return a string representation of the list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

if __name__ == "__main__":
    ll = SinglyLinkedList()
    print("Initial list:", ll if ll.head else "Empty")

    print("Appending 1, 2, 3...")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("List:", ll)

    print("Prepending 0...")
    ll.prepend(0)
    print("List:", ll)

    print("Deleting 2...")
    ll.delete(2)
    print("List:", ll)

    print("Reversing list...")
    ll.reverse()
    print("List:", ll)
