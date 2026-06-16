"""
A complete, runnable Python program implementing a Trie (Prefix Tree).
This module provides a Trie class with insertion, exact search, and prefix search capabilities.
"""

class TrieNode:
    """
    A node in the Trie.
    """
    def __init__(self):
        """
        Initialize the Trie node with a dictionary for children and a boolean for end of word.
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie (Prefix Tree) data structure.
    """
    def __init__(self):
        """
        Initialize the Trie with a root node.
        """
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
        Returns True if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    # Demonstration of the Trie
    trie = Trie()
    
    words_to_insert = ["apple", "app", "application", "banana", "bat"]
    print(f"Inserting words: {words_to_insert}")
    for w in words_to_insert:
        trie.insert(w)
    
    # Test cases
    test_search = ["apple", "app", "appl", "batman", "banana"]
    print("\\n--- Search Tests ---")
    for w in test_search:
        print(f"Search '{w}': {trie.search(w)}")
        
    test_prefix = ["app", "ban", "cat", "ba"]
    print("\\n--- Prefix Search Tests ---")
    for p in test_prefix:
        print(f"Starts with '{p}': {trie.starts_with(p)}")
