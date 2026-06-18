"""
Singly Linked List Implementation
This module provides a basic implementation of a singly linked list data structure
with common operations such as append, prepend, delete, and reverse.
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

class SinglyLinkedList:
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
        Delete the first occurrence of a node with the given data (key).
        """
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
        print(" -> ".join(elements) if elements else "Empty List")

if __name__ == "__main__":
    # Demo of SinglyLinkedList
    sll = SinglyLinkedList()
    
    print("Appending 10, 20, 30:")
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.display()

    print("\nPrepending 5:")
    sll.prepend(5)
    sll.display()

    print("\nDeleting 20:")
    sll.delete(20)
    sll.display()

    print("\nReversing the list:")
    sll.reverse()
    sll.display()
