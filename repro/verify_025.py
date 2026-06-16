"""
Module for a Trie (Prefix Tree) implementation.
This module provides a Trie class with methods for insertion, exact search,
and prefix search (starts_with).
"""

class TrieNode:
    """A node in the Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """A Trie (Prefix Tree) data structure."""
    def __init__(self):
        """Initialize the trie."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == '__main__':
    # Demonstration of the Trie
    trie = Trie()
    words = ["apple", "app", "application", "banana", "bat"]
    
    print("Inserting words:", words)
    for w in words:
        trie.insert(w)
    
    print("\\nSearch results:")
    print(f"Search 'apple': {trie.search('apple')}")        # True
    print(f"Search 'app': {trie.search('app')}")            # True
    print(f"Search 'appl': {trie.search('appl')}")          # False
    print(f"Search 'banana': {trie.search('banana')}")      # True
    print(f"Search 'band': {trie.search('band')}")          # False
    
    print("\\nStarts with results:")
    print(f"Starts with 'app': {trie.starts_with('app')}")   # True
    print(f"Starts with 'ban': {trie.starts_with('ban')}")   # True
    print(f"Starts with 'cat': {trie.starts_with('cat')}")   # False
