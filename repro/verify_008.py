"""
Binary Search Tree (BST) Implementation.

This module provides a basic implementation of a Binary Search Tree with
insertion, searching, and inorder traversal.
"""

class Node:
    """
    A node in the Binary Search Tree.
    """
    def __init__(self, key):
        """
        Initialize a node with a key.
        """
        self.left = None
        self.right = None
        self.val = key

class BST:
    """
    Binary Search Tree implementation.
    """
    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, key):
        """
        Insert a key into the BST.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
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
        Search for a key in the BST. Returns True if found, False otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """
        Perform an inorder traversal and return the list of keys.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    # Demonstration
    tree = BST()
    elements = [50, 30, 20, 40, 70, 60, 80]
    for el in elements:
        tree.insert(el)

    print("Inorder Traversal:", tree.inorder_traversal())
    print("Search for 40:", tree.search(40))
    print("Search for 100:", tree.search(100))
