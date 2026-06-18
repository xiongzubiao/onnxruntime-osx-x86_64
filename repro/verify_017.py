"""
A complete, runnable Python program implementing a Trie (Prefix Tree).
This module provides a Trie class with methods for insertion, search, and prefix matching.
"""

class TrieNode:
    """Represents a node in the Trie."""
    def __init__(self):
        """Initializes a TrieNode with an empty dictionary of children and is_end_of_word flag."""
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """A Trie (Prefix Tree) implementation."""
    def __init__(self):
        """Initializes the Trie with a root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        
        Args:
            word: The word to be inserted.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.
        
        Args:
            word: The word to search for.
            
        Returns:
            True if the word is in the Trie, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that starts with the given prefix.
        
        Args:
            prefix: The prefix to check.
            
        Returns:
            True if there is a word with the prefix, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    # Demonstration of the Trie implementation
    trie = Trie()
    
    print("Inserting words: 'apple', 'app'")
    trie.insert("apple")
    trie.insert("app")
    
    print(f"Search 'apple': {trie.search('apple')}")   # Expected: True
    print(f"Search 'app': {trie.search('app')}")       # Expected: True
    print(f"Search 'appl': {trie.search('appl')}")     # Expected: False
    
    print(f"Starts with 'app': {trie.starts_with('app')}") # Expected: True
    print(f"Starts with 'apq': {trie.starts_with('apq')}") # Expected: False
    
    trie.insert("beer")
    print(f"Search 'beer': {trie.search('beer')}")     # Expected: True
    print(f"Starts with 'be': {trie.starts_with('be')}") # Expected: True
