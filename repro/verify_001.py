"""
A complete, runnable Python implementation of a Trie (Prefix Tree) data structure.
This module provides classes for TrieNode and the Trie itself, supporting
insertion, full-word search, and prefix matching.
"""

class TrieNode:
    """
    Represents a single node in the Trie.
    Each node contains a dictionary of children and a boolean flag
    indicating if the node marks the end of a complete word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Trie (Prefix Tree) implementation for efficient string storage and retrieval.
    """
    def __init__(self):
        """
        Initialize the Trie with a root node.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        Iterates through each character, creating new nodes as necessary.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the Trie, False otherwise.
        Matches the full word from the root.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the Trie that starts with the given prefix.
        Similar to search, but does not require the is_end_of_word flag.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    # Demonstration of Trie functionality
    print("--- Trie Implementation Demo ---")
    trie = Trie()
    
    words_to_insert = ["apple", "app", "application", "banana"]
    print(f"Inserting words: {words_to_insert}")
    for w in words_to_insert:
        trie.insert(w)

    # Search tests
    print(f"Search 'apple': {trie.search('apple')}")      # Expected: True
    print(f"Search 'appl': {trie.search('appl')}")       # Expected: False
    print(f"Search 'banana': {trie.search('banana')}")    # Expected: True
    print(f"Search 'orange': {trie.search('orange')}")    # Expected: False

    # Prefix tests
    print(f"Starts with 'app': {trie.starts_with('app')}") # Expected: True
    print(f"Starts with 'ban': {trie.starts_with('ban')}") # Expected: True
    print(f"Starts with 'cat': {trie.starts_with('cat')}") # Expected: False
    
    print("\nDemo completed.")
