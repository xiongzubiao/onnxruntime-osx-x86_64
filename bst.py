class Node:
    """
    A class representing a node in a Binary Search Tree.
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    """
    A class representing a Binary Search Tree (BST).
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Inserts a new key into the BST.
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
        Searches for a key in the BST. Returns the node if found, else None.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """
        Returns a list of values in the BST in inorder.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

def main():
    """
    Demo function for the BST class.
    """
    bst = BST()
    values = [50, 30, 20, 40, 70, 60, 80]
    
    print(f"Inserting values: {values}")
    for v in values:
        bst.insert(v)
    
    print("Inorder Traversal:", bst.inorder_traversal())
    
    search_key = 40
    result = bst.search(search_key)
    if result:
        print(f"Key {search_key} found in the tree.")
    else:
        print(f"Key {search_key} not found in the tree.")

if __name__ == "__main__":
    main()
