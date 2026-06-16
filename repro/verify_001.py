"""
Trie (Prefix Tree) Implementation.

This module provides a complete, runnable implementation of a Trie data structure,
which is an efficient information retrieval data structure. It supports
inserting strings, searching for strings, and checking for prefixes.
"""

class TrieNode:
    """A node in the Trie data structure."""
    
    def __init__(self):
        """Initialize the TrieNode with an empty children dictionary and is_end_of_word flag."""
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Trie (Prefix Tree) implementation."""

    def __init__(self):
        """Initialize the Trie with a root TrieNode."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        
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
        Returns if the word is in the trie.
        
        Args:
            word: The word to search for.
            
        Returns:
            True if the word exists in the trie, False otherwise.
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
            prefix: The prefix to check for.
            
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
    # Demo of the Trie implementation
    trie = Trie()
    
    words_to_insert = ["apple", "app", "application", "banana", "bat"]
    print(f"Inserting words: {words_to_insert}")
    for word in words_to_insert:
        trie.insert(word)
        
    search_tests = ["apple", "app", "appl", "banana", "batman"]
    print("\\nSearch results:")
    for word in search_tests:
        print(f"Search '{word}': {trie.search(word)}")
        
    prefix_tests = ["app", "ban", "cat", "bat"]
    print("\\nPrefix search results:")
    for prefix in prefix_tests:
        print(f"Starts with '{prefix}': {trie.starts_with(prefix)}")
