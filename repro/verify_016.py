"""
Binary Search Tree (BST) implementation module.

This module provides a basic implementation of a Binary Search Tree with
insertion, search, and inorder traversal capabilities.
"""

from __future__ import annotations
from typing import Any, Optional, List


class Node:
    """
    A node in the Binary Search Tree.
    """

    def __init__(self, value: Any):
        """
        Initialize a new Node with a value.

        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    """
    A Binary Search Tree implementation.
    """

    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root: Optional[Node] = None

    def insert(self, value: Any) -> None:
        """
        Insert a value into the BST.

        Args:
            value: The value to insert.
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
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value: Any) -> bool:
        """
        Search for a value in the BST.

        Args:
            value: The value to search for.

        Returns:
            True if the value is found, False otherwise.
        """
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
        """
        Perform an inorder traversal of the BST.

        Returns:
            A list of values in sorted order.
        """
        result: List[Any] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current: Optional[Node], result: List[Any]) -> None:
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.value)
            self._inorder_recursive(current.right, result)


if __name__ == "__main__":
    # Create a BST instance
    bst = BST()

    # Insert some values
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values: {values_to_insert}")
    for val in values_to_insert:
        bst.insert(val)

    # Search for values
    search_values = [40, 90]
    for val in search_values:
        found = bst.search(val)
        print(f"Searching for {val}: {'Found' if found else 'Not Found'}")

    # Display inorder traversal
    inorder = bst.inorder_traversal()
    print(f"Inorder traversal: {inorder}")
