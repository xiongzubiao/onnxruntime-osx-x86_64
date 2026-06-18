"""
Singly Linked List Implementation.
This module provides a basic implementation of a singly linked list with 
methods to append, prepend, delete, and reverse.
"""

class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, data):
        """Initialize a node with data and set next to None."""
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Add a node with the specified data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Add a node with the specified data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first node that contains the specified key."""
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        while current:
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
        print(" -> ".join(elements))

if __name__ == "__main__":
    # Demonstration of SinglyLinkedList functionality
    llist = SinglyLinkedList()
    print("Appending 10, 20, 30:")
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.display()

    print("Prepending 5:")
    llist.prepend(5)
    llist.display()

    print("Deleting 20:")
    llist.delete(20)
    llist.display()

    print("Reversing list:")
    llist.reverse()
    llist.display()
