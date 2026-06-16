"""
Singly Linked List Implementation.

This module provides a complete, runnable implementation of a singly linked list
data structure with operations for appending, prepending, deleting nodes,
and reversing the list.
"""

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        """Initialize a node with data and a null next pointer."""
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list class."""
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
        """Delete the first occurrence of a node with the specified data (key)."""
        temp = self.head

        # Case 1: Head node itself holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Case 2: Search for the key to be deleted
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Key not found
        if temp is None:
            return

        # Unlink the node from linked list
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

    def display(self):
        """Print the elements of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")

if __name__ == "__main__":
    print("--- Singly Linked List Demo ---")
    llist = LinkedList()

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
