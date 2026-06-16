"""Binary Search Tree (BST) Implementation.

This module provides a complete implementation of a Binary Search Tree,
including classes for nodes and the tree itself, with methods for insertion,
searching, and inorder traversal.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Node:
    """A node in a binary search tree."""
    value: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


class BST:
    """A binary search tree supporting insertion, search, and traversal."""

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self.root: Optional[Node] = None

    def insert(self, value: Any) -> None:
        """Insert a value into the tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: Node, value: Any) -> None:
        """Helper method to insert a value recursively."""
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value: Any) -> bool:
        """Search for a value in the tree. Returns True if found, False otherwise."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current: Optional[Node], value: Any) -> bool:
        """Helper method to search for a value recursively."""
        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    def inorder_traversal(self) -> List[Any]:
        """Perform an inorder traversal and return the list of values."""
        values: List[Any] = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, current: Optional[Node], values: List[Any]) -> None:
        """Helper method to perform inorder traversal recursively."""
        if current:
            self._inorder_recursive(current.left, values)
            values.append(current.value)
            self._inorder_recursive(current.right, values)


if __name__ == "__main__":
    # Demonstration of the BST implementation
    tree = BST()
    data = [5, 3, 7, 2, 4, 6, 8]
    
    print(f"Inserting values: {data}")
    for x in data:
        tree.insert(x)
    
    print(f"Inorder Traversal: {tree.inorder_traversal()}")
    
    search_values = [4, 9]
    for val in search_values:
        found = tree.search(val)
        print(f"Searching for {val}: {'Found' if found else 'Not Found'}")
