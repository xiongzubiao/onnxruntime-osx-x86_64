"""
This module provides a basic implementation of a Trie (prefix tree) data structure.
A Trie is an efficient information retrieval data structure. Using Trie, search 
complexities can be brought to optimal limit (key length).
"""

class TrieNode:
    """
    A node in the Trie.
    """
    def __init__(self):
        """
        Initialize the Trie node with a dictionary for children and a boolean 
        to indicate the end of a word.
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Trie data structure implementation.
    """
    def __init__(self):
        """
        Initialize the trie object.
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

if __name__ == "__main__":
    # Demonstration of the Trie data structure
    trie = Trie()
    
    words_to_insert = ["apple", "app", "application", "banana", "bat"]
    print(f"Inserting words: {words_to_insert}")
    for w in words_to_insert:
        trie.insert(w)
        
    print("\nSearch results:")
    print(f"Search 'apple': {trie.search('apple')}")  # Expected: True
    print(f"Search 'app': {trie.search('app')}")      # Expected: True
    print(f"Search 'appl': {trie.search('appl')}")    # Expected: False
    print(f"Search 'batman': {trie.search('batman')}")# Expected: False
    
    print("\nPrefix search results:")
    print(f"Starts with 'app': {trie.starts_with('app')}")   # Expected: True
    print(f"Starts with 'ban': {trie.starts_with('ban')}")   # Expected: True
    print(f"Starts with 'cat': {trie.starts_with('cat')}")   # Expected: False
