"""
A module for implementing and demonstrating a Binary Search Tree (BST).
"""

class Node:
    """
    A class representing a node in a Binary Search Tree.
    """
    def __init__(self, key):
        """
        Initializes a node with a given key.

        Args:
            key: The value to be stored in the node.
        """
        self.left = None
        self.right = None
        self.val = key

class BST:
    """
    A class representing a Binary Search Tree.
    """
    def __init__(self):
        """Initializes an empty Binary Search Tree."""
        self.root = None

    def insert(self, key):
        """
        Inserts a key into the BST.

        Args:
            key: The value to insert.
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
        Searches for a key in the BST.

        Args:
            key: The value to search for.

        Returns:
            bool: True if found, False otherwise.
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
        Performs an inorder traversal of the BST.

        Returns:
            list: The keys in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

if __name__ == '__main__':
    # Demo
    tree = BST()
    elements = [50, 30, 20, 40, 70, 60, 80]
    for e in elements:
        tree.insert(e)

    print("Inorder Traversal:", tree.inorder_traversal())
    print("Search 40:", tree.search(40))
    print("Search 100:", tree.search(100))
