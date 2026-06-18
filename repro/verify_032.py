"""
Binary Search Tree (BST) Implementation
This module provides a basic implementation of a Binary Search Tree with
insertion, search, and inorder traversal capabilities.
"""

class Node:
    """
    A class representing a node in a binary search tree.
    """
    def __init__(self, key):
        """
        Initialize a node with a key and empty children.
        :param key: The value to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None

class BST:
    """
    A class representing a binary search tree.
    """
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    def insert(self, key):
        """
        Insert a new key into the BST.
        :param key: The value to insert.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
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
        :param key: The value to search for.
        :return: True if found, False otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
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
        :return: A list of keys in ascending order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    # Demonstration of the BST implementation
    bst = BST()
    keys = [50, 30, 20, 40, 70, 60, 80]

    print(f"Inserting keys: {keys}")
    for k in keys:
        bst.insert(k)

    print(f"Inorder Traversal: {bst.inorder_traversal()}")

    search_keys = [20, 55, 80]
    for sk in search_keys:
        found = bst.search(sk)
        print(f"Search for {sk}: {'Found' if found else 'Not Found'}")
