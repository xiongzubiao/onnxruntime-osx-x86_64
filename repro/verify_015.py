"""
Singly Linked List Implementation.

This module provides a complete, runnable implementation of a singly linked list
data structure with operations for appending, prepending, deleting nodes,
and reversing the list.
"""

class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, data):
        """Initialize a node with data and a null next pointer."""
        self.data = data
        self.next = None

class LinkedList:
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

        # Case 1: Head node holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Case 2: Search for the key
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Case 3: Key not found
        if temp is None:
            return

        # Unlink the node
        prev.next = temp.next
        temp = None

    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        """Return a list representation of the linked list for easy viewing."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

if __name__ == "__main__":
    # Demo of the Singly Linked List
    llist = LinkedList()

    print("Initial list (empty):", llist.display())

    llist.append(10)
    llist.append(20)
    llist.append(30)
    print("After appending 10, 20, 30:", llist.display())

    llist.prepend(5)
    print("After prepending 5:", llist.display())

    llist.delete(20)
    print("After deleting 20:", llist.display())

    llist.reverse()
    print("After reversing the list:", llist.display())
