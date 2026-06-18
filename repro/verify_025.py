"""
A complete, runnable Python program implementing a Trie data structure.
This module provides a Trie class with support for insertion, search, and prefix matching.
"""

class TrieNode:
    """
    A node in the Trie.
    """
    def __init__(self):
        """
        Initialize the Trie node.
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie (prefix tree) implementation.
    """
    def __init__(self):
        """
        Initialize the Trie.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        
        :param word: The word to insert.
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
        
        :param word: The word to search for.
        :return: True if the word is in the trie, False otherwise.
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
        
        :param prefix: The prefix to check.
        :return: True if any word starts with the prefix, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    # Demonstration of the Trie functionality
    trie = Trie()
    
    print("Inserting words: 'apple', 'app', 'application'")
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")
    
    print(f"Search 'apple': {trie.search('apple')}")        # Expected: True
    print(f"Search 'app': {trie.search('app')}")            # Expected: True
    print(f"Search 'appl': {trie.search('appl')}")          # Expected: False
    print(f"Starts with 'appl': {trie.starts_with('appl')}") # Expected: True
    print(f"Starts with 'ban': {trie.starts_with('ban')}")   # Expected: False
    
    print("\nInserting word: 'banana'")
    trie.insert("banana")
    print(f"Search 'banana': {trie.search('banana')}")      # Expected: True
