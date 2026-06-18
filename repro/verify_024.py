"""
Binary Search Tree (BST) Implementation.

This module provides a basic implementation of a Binary Search Tree with
functionalities for inserting nodes, searching for values, and performing
an inorder traversal to retrieve sorted values.
"""

class Node:
    """
    A class representing a single node in a Binary Search Tree.
    """
    def __init__(self, key):
        """
        Initialize a node with a key and no children.

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
        """
        Initialize an empty Binary Search Tree.
        """
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

    def _insert_recursive(self, current_node, key):
        """
        Helper method to recursively find the correct position for a new key.
        """
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        # Duplicate keys are ignored in this implementation

    def search(self, key):
        """
        Search for a key in the BST.

        Args:
            key: The value to search for.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        """
        Helper method to recursively search for a key.
        """
        if current_node is None:
            return False
        if current_node.key == key:
            return True
        if key < current_node.key:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the BST.

        Returns:
            list: A list of keys in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        """
        Helper method to recursively perform inorder traversal.
        """
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.key)
            self._inorder_recursive(current_node.right, result)

if __name__ == "__main__":
    # Demonstration of BST functionality
    bst = BST()
    
    # Insert elements
    elements = [50, 30, 20, 40, 70, 60, 80]
    print(f"Inserting elements: {elements}")
    for el in elements:
        bst.insert(el)
    
    # Inorder Traversal (should be sorted)
    print(f"Inorder Traversal: {bst.inorder_traversal()}")
    
    # Search elements
    search_keys = [40, 90]
    for key in search_keys:
        found = bst.search(key)
        print(f"Searching for {key}: {'Found' if found else 'Not Found'}")
