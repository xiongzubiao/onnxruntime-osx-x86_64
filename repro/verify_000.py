"""
Binary Search Tree (BST) Implementation.

This module provides a basic implementation of a Binary Search Tree with
insertion, search, and inorder traversal capabilities.
"""

from typing import Optional, Any

class Node:
    """
    A class representing a node in a Binary Search Tree.
    """
    def __init__(self, key: Any):
        """
        Initialize a node with a key and no children.
        
        Args:
            key: The value to be stored in the node.
        """
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BST:
    """
    A class representing a Binary Search Tree.
    """
    def __init__(self):
        """Initialize an empty BST."""
        self.root: Optional[Node] = None

    def insert(self, key: Any) -> None:
        """
        Insert a key into the BST.
        
        Args:
            key: The value to be inserted.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current: Node, key: Any) -> None:
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def search(self, key: Any) -> bool:
        """
        Search for a key in the BST.
        
        Args:
            key: The value to search for.
            
        Returns:
            True if the key is found, False otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current: Optional[Node], key: Any) -> bool:
        if current is None:
            return False
        if current.key == key:
            return True
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    def inorder_traversal(self) -> list:
        """
        Perform an inorder traversal of the BST.
        
        Returns:
            A list of keys in ascending order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current: Optional[Node], result: list) -> None:
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.key)
            self._inorder_recursive(current.right, result)

if __name__ == "__main__":
    # Demo
    bst = BST()
    elements = [50, 30, 20, 40, 70, 60, 80]
    
    print(f"Inserting elements: {elements}")
    for el in elements:
        bst.insert(el)
    
    print(f"Inorder traversal: {bst.inorder_traversal()}")
    
    search_keys = [40, 90]
    for key in search_keys:
        found = bst.search(key)
        print(f"Searching for {key}: {'Found' if found else 'Not Found'}")
