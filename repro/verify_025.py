"""
A complete, runnable Python program implementing a Trie (Prefix Tree).
This module provides a Trie class with insertion, search, and prefix matching capabilities.
"""

class TrieNode:
    """A node in the Trie data structure."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Trie data structure implementation."""

    def __init__(self):
        """Initialize the trie with a root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        
        Args:
            word: The string to be inserted.
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
        
        Args:
            word: The string to search for.
            
        Returns:
            True if the word exists, False otherwise.
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
        
        Args:
            prefix: The prefix string to check.
            
        Returns:
            True if any word starts with the prefix, False otherwise.
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
    
    print("--- Trie Demonstration ---")
    
    words_to_insert = ["apple", "app", "application", "banana", "bat"]
    print(f"Inserting words: {', '.join(words_to_insert)}")
    for w in words_to_insert:
        trie.insert(w)
    
    # Test Search
    search_queries = ["apple", "app", "appl", "orange"]
    for q in search_queries:
        print(f"Search '{q}': {trie.search(q)}")
    
    # Test Starts With
    prefix_queries = ["app", "ban", "cat"]
    for p in prefix_queries:
        print(f"Starts with '{p}': {trie.starts_with(p)}")
