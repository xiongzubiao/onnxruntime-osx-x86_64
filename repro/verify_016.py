"""
Binary Search Tree (BST) Implementation.

This module provides a basic implementation of a Binary Search Tree with
insertion, search, and in-order traversal capabilities.
"""

class Node:
    """
    A class representing a node in a Binary Search Tree.
    """
    def __init__(self, key):
        """
        Initialize the node with a key and no children.
        
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
        Insert a key into the BST.
        
        Args:
            key: The value to insert.
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
        
        Args:
            key: The value to search for.
            
        Returns:
            bool: True if the key exists, False otherwise.
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
        Perform an in-order traversal of the BST.
        
        Returns:
            list: A list of keys in ascending order.
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
    # Demonstration of the BST
    bst = BST()
    elements = [50, 30, 20, 40, 70, 60, 80]
    print(f"Inserting elements: {elements}")
    for el in elements:
        bst.insert(el)
    
    print(f"In-order Traversal: {bst.inorder_traversal()}")
    
    search_key = 40
    print(f"Searching for {search_key}: {'Found' if bst.search(search_key) else 'Not Found'}")
    
    search_key = 100
    print(f"Searching for {search_key}: {'Found' if bst.search(search_key) else 'Not Found'}")
