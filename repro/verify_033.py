"""
A complete, runnable Python program implementing a Trie (Prefix Tree) data structure.
This module provides a Trie class with support for word insertion, search, and
prefix matching.
"""

class TrieNode:
    """
    A node in the Trie structure.
    """
    def __init__(self):
        """
        Initializes a TrieNode with an empty children dictionary and is_end_of_word flag.
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie (Prefix Tree) implementation for efficient string storage and retrieval.
    """
    def __init__(self):
        """
        Initializes the Trie with a root node.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        
        Args:
            word (str): The word to insert.
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
            word (str): The word to search for.
            
        Returns:
            bool: True if the word exists in the Trie, False otherwise.
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
            prefix (str): The prefix to check for.
            
        Returns:
            bool: True if such a word exists, False otherwise.
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
    
    words_to_insert = ["apple", "app", "application", "banana", "bat", "batch"]
    print(f"Inserting words: {words_to_insert}")
    for word in words_to_insert:
        trie.insert(word)
    
    # Test search
    search_tests = ["apple", "app", "appl", "banana", "batman"]
    print("\nSearch results:")
    for test in search_tests:
        print(f"Searching for '{test}': {trie.search(test)}")
        
    # Test starts_with
    prefix_tests = ["app", "ban", "cat", "batch"]
    print("\nPrefix match results:")
    for prefix in prefix_tests:
        print(f"Starts with '{prefix}': {trie.starts_with(prefix)}")
