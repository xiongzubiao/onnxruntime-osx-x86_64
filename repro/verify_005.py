"""
LRU Cache Implementation.

This module provides a Least Recently Used (LRU) cache using collections.OrderedDict.
"""

from collections import OrderedDict

class LRUCache:
    """
    A simple LRU Cache implementation using OrderedDict.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache with a given capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieve an item from the cache.

        Args:
            key (int): The key of the item to retrieve.

        Returns:
            int: The value associated with the key, or -1 if not found.
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Insert or update an item in the cache.

        Args:
            key (int): The key of the item.
            value (int): The value to store.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    # Demo
    print("Initializing LRU Cache with capacity 2")
    lru = LRUCache(2)
    
    print("Putting (1, 1)")
    lru.put(1, 1)
    print("Putting (2, 2)")
    lru.put(2, 2)
    
    print(f"Getting 1: {lru.get(1)}")  # returns 1
    
    print("Putting (3, 3) - evicts 2")
    lru.put(3, 3)
    
    print(f"Getting 2: {lru.get(2)}")  # returns -1 (evicted)
    
    print("Putting (4, 4) - evicts 1")
    lru.put(4, 4)
    
    print(f"Getting 1: {lru.get(1)}")  # returns -1 (evicted)
    print(f"Getting 3: {lru.get(3)}")  # returns 3
    print(f"Getting 4: {lru.get(4)}")  # returns 4
