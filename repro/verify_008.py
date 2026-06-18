"""
Binary Search Tree (BST) Implementation
This module provides a complete, runnable implementation of a Binary Search Tree
with support for insertion, searching, and inorder traversal.
"""

class Node:
    """
    A class representing a node in a binary search tree.
    """
    def __init__(self, key):
        """
        Initialize a new node with a given key.
        
        Args:
            key: The value to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None


class BST:
    """
    A class representing a Binary Search Tree.
    """
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, key):
        """
        Insert a new key into the BST.
        
        Args:
            key: The value to insert.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Helper method to insert a key recursively."""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """
        Search for a key in the BST.
        
        Args:
            key: The value to search for.
            
        Returns:
            bool: True if the key is found, False otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """Helper method to search for a key recursively."""
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the BST.
        
        Returns:
            list: A list of keys in ascending order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    # Demonstration of the BST implementation
    print("--- Binary Search Tree Demo ---")
    bst = BST()
    
    # Inserting values
    values_to_insert = [50, 30, 20, 40, 70, 60, 80]
    print(f"Inserting values: {values_to_insert}")
    for val in values_to_insert:
        bst.insert(val)
    
    # Inorder traversal
    ordered_list = bst.inorder_traversal()
    print(f"Inorder traversal result: {ordered_list}")
    
    # Searching
    search_keys = [40, 90]
    for key in search_keys:
        found = bst.search(key)
        print(f"Searching for {key}: {'Found' if found else 'Not Found'}")
