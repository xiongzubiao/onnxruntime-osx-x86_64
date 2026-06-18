"""
A complete, runnable Python program implementing a binary search tree (BST).
"""

class Node:
    """
    A class representing a node in a binary search tree.
    """
    def __init__(self, key):
        """
        Initialize the node with a key and no children.
        """
        self.left = None
        self.right = None
        self.val = key

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
        Insert a key into the binary search tree.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """
        Search for a key in the binary search tree.
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary search tree.
        """
        res = []
        self._inorder_traversal(self.root, res)
        return res

    def _inorder_traversal(self, node, res):
        if node:
            self._inorder_traversal(node.left, res)
            res.append(node.val)
            self._inorder_traversal(node.right, res)

if __name__ == '__main__':
    # Demo
    bst = BST()
    elements = [50, 30, 20, 40, 70, 60, 80]
    for el in elements:
        bst.insert(el)

    print("Inorder traversal:", bst.inorder_traversal())
    
    search_key = 40
    result = bst.search(search_key)
    if result:
        print(f"Key {search_key} found in the tree.")
    else:
        print(f"Key {search_key} not found in the tree.")
