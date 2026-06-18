"""
Binary Search Tree (BST) Implementation
This module provides a basic implementation of a Binary Search Tree with 
insertion, search, and inorder traversal capabilities.
"""

class Node:
    """
    A class representing a single node in a Binary Search Tree.
    """
    def __init__(self, key):
        """
        Initialize a node with a key and no children.
        :param key: The value to store in the node.
        """
        self.left = None
        self.right = None
        self.val = key

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
        :param key: The value to insert.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """
        Helper method to insert a key recursively.
        """
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
        Search for a key in the BST.
        :param key: The value to search for.
        :return: True if found, False otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """
        Helper method to search for a key recursively.
        """
        if node is None:
            return False
        if node.val == key:
            return True
        if key < node.val:
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
        """
        Helper method for inorder traversal.
        """
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

if __name__ == '__main__':
    # Demonstration of the BST
    bst = BST()
    elements = [50, 30, 20, 40, 70, 60, 80]
    
    print(f"Inserting elements: {elements}")
    for el in elements:
        bst.insert(el)
    
    print("Inorder Traversal (Sorted):", bst.inorder_traversal())
    
    search_keys = [40, 90]
    for key in search_keys:
        found = bst.search(key)
        print(f"Searching for {key}: {'Found' if found else 'Not Found'}")
