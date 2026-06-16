"""
Singly Linked List Implementation.

This module provides a complete, runnable implementation of a singly linked list
data structure with operations for appending, prepending, deleting nodes,
and reversing the list.
"""

class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: A reference to the next node in the list.
    """
    def __init__(self, data):
        """
        Initializes a new node with the given data.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Appends a new node with the specified data to the end of the list.
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
        Prepends a new node with the specified data to the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Deletes the first occurrence of a node with the specified data (key).
        """
        current = self.head
        
        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key was not present in linked list
        if current is None:
            return

        # Unlink the node from linked list
        prev.next = current.next
        current = None

    def reverse(self):
        """
        Reverses the linked list in-place.
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
        Returns a string representation of the list elements.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"


if __name__ == "__main__":
    # Demonstration of LinkedList operations
    print("--- Singly Linked List Demo ---")
    llist = LinkedList()
    
    print("Appending 10, 20, 30...")
    llist.append(10)
    llist.append(20)
    llist.append(30)
    print(f"List: {llist.display()}")

    print("\nPrepending 5...")
    llist.prepend(5)
    print(f"List: {llist.display()}")

    print("\nDeleting 20...")
    llist.delete(20)
    print(f"List: {llist.display()}")

    print("\nReversing the list...")
    llist.reverse()
    print(f"List: {llist.display()}")
