"""
Module for Binary Search Tree (BST) implementation.
This module provides a basic BST with insertion, search, and inorder traversal.
"""

class Node:
    """A node in a Binary Search Tree."""
    def __init__(self, key):
        """Initialize a node with a key and no children."""
        self.key = key
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree implementation."""
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        """Helper method to recursively insert a key."""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """Search for a key in the BST. Returns the node if found, else None."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Helper method to recursively search for a key."""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        """Perform inorder traversal and return keys as a list."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Helper method for recursive inorder traversal."""
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

if __name__ == '__main__':
    # Demonstration of the BST implementation
    bst = BST()
    # Inserting values
    keys_to_insert = [50, 30, 20, 40, 70, 60, 80]
    print(f"Inserting keys: {keys_to_insert}")
    for k in keys_to_insert:
        bst.insert(k)
    
    # Inorder Traversal
    print("Inorder traversal (should be sorted):", bst.inorder_traversal())
    
    # Searching
    for search_key in [40, 99]:
        found_node = bst.search(search_key)
        status = "Found" if found_node else "Not Found"
        print(f"Searching for {search_key}: {status}")
