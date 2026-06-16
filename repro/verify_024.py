"""Binary Search Tree (BST) implementation.

This module provides a complete, runnable example of a binary search tree
with insertion, search, and inorder traversal operations.
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
        """Insert a value into the tree.

        Duplicate values are typically placed in the right subtree in this implementation.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: Node, value: Any) -> None:
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
        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    def inorder_traversal(self) -> List[Any]:
        """Return the values in the tree in sorted order using inorder traversal."""
        result: List[Any] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current: Optional[Node], result: List[Any]) -> None:
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.value)
            self._inorder_recursive(current.right, result)


if __name__ == "__main__":
    # Demo of BST functionality
    bst = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    
    print(f"Inserting values: {values_to_insert}")
    for val in values_to_insert:
        bst.insert(val)

    print(f"Inorder traversal (sorted): {bst.inorder_traversal()}")

    search_values = [40, 90]
    for val in search_values:
        found = bst.search(val)
        print(f"Searching for {val}: {'Found' if found else 'Not Found'}")
