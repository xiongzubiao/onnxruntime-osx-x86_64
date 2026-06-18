"""
Singly Linked List Implementation Module.

This module provides a SinglyLinkedList class and a Node class to implement
a basic singly linked list with common operations such as append, prepend,
delete, and reverse.
"""

class Node:
    """
    Represents a node in a singly linked list.
    """
    def __init__(self, data):
        """
        Initializes a node with data and a pointer to the next node.
        
        Args:
            data: The value to be stored in the node.
        """
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    Represents a singly linked list data structure.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def append(self, data):
        """
        Adds a new node with data to the end of the list.
        
        Args:
            data: The value to be appended.
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
        Adds a new node with data to the beginning of the list.
        
        Args:
            data: The value to be prepended.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        Removes the first node containing the specified data.
        
        Args:
            data: The value to be removed from the list.
        """
        temp = self.head

        # If head node itself holds the data to be deleted
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        # Search for the data to be deleted, keep track of the previous node
        prev = None
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        # If data was not present in the list
        if temp is None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def reverse(self):
        """
        Reverses the linked list in-place.
        """
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        nodes.append("None")
        return " -> ".join(nodes)

if __name__ == "__main__":
    # Demo implementation of the SinglyLinkedList
    llist = SinglyLinkedList()
    print("Initial list (empty):", llist)
    
    print("\nAppending 1, 2, 3...")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print("List after appends:", llist)
    
    print("\nPrepending 0...")
    llist.prepend(0)
    print("List after prepend:", llist)
    
    print("\nDeleting 2...")
    llist.delete(2)
    print("List after deletion of 2:", llist)
    
    print("\nReversing list...")
    llist.reverse()
    print("List after reversal:", llist)
