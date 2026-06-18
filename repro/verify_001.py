"""
This module provides a complete, runnable implementation of a Trie (Prefix Tree) data structure.
The Trie supports word insertion, exact word search, and prefix matching.
"""

class TrieNode:
    """
    A node in the Trie. Contains a dictionary of children and a boolean flag
    indicating if the node marks the end of a complete word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie (Prefix Tree) implementation for efficient string retrieval.
    """

    def __init__(self):
        """
        Initializes the Trie with an empty root node.
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
        Searches for an exact word in the Trie.
        
        Args:
            word (str): The word to search for.
            
        Returns:
            bool: True if the word is found, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Checks if any word in the Trie starts with the given prefix.
        
        Args:
            prefix (str): The prefix to check.
            
        Returns:
            bool: True if any word starts with the prefix, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    # Demonstration of the Trie functionality
    print("--- Trie Demonstration ---")
    my_trie = Trie()
    
    words_to_insert = ["apple", "app", "application", "banana"]
    print(f"Inserting words: {words_to_insert}")
    for w in words_to_insert:
        my_trie.insert(w)
        
    # Test Search
    test_search = ["apple", "app", "appl", "orange"]
    for s in test_search:
        print(f"Search for '{s}': {my_trie.search(s)}")
        
    # Test Prefix Matching
    test_prefixes = ["app", "ban", "bat"]
    for p in test_prefixes:
        print(f"Starts with prefix '{p}': {my_trie.starts_with(p)}")
