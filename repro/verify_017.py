"""
This module provides a basic implementation of a Trie (Prefix Tree) data structure.
A Trie is an efficient information retrieval data structure that can be used to
store a dynamic set or associative array where the keys are usually strings.
"""

class TrieNode:
    """
    A node in the Trie.
    """
    def __init__(self):
        """
        Initializes a TrieNode with an empty children dictionary and a boolean
        flag indicating the end of a word.
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Trie data structure implementation.
    """
    def __init__(self):
        """
        Initializes the Trie with a root node.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        
        Args:
            word (str): The word to be inserted.
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
            word (str): The word to search for.
            
        Returns:
            bool: True if the word is in the trie, False otherwise.
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
            prefix (str): The prefix to search for.
            
        Returns:
            bool: True if there is a word with the prefix, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == '__main__':
    # Demonstration of the Trie implementation
    trie = Trie()
    
    words_to_insert = ["apple", "app", "application", "bat", "batch"]
    print(f"Inserting words: {words_to_insert}")
    for w in words_to_insert:
        trie.insert(w)
    
    test_searches = ["apple", "app", "appl", "bat", "ball"]
    print("\nSearch results:")
    for w in test_searches:
        print(f"Search '{w}': {trie.search(w)}")
        
    test_prefixes = ["app", "appl", "ba", "cat"]
    print("\nPrefix search (starts_with) results:")
    for p in test_prefixes:
        print(f"Starts with '{p}': {trie.starts_with(p)}")
