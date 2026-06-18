"""
This module provides a simple implementation of an LRU (Least Recently Used) cache
using the collections.OrderedDict class.
"""

from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache implementation.
    
    The cache has a fixed capacity. When the capacity is reached, the least
    recently used item is removed to make space for new items.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        Retrieve an item from the cache.

        If the key exists, it is moved to the end (most recently used).
        
        Args:
            key: The key to look up in the cache.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if key not in self.cache:
            return None
        # Move the accessed item to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Add or update an item in the cache.

        If the key already exists, its value is updated and it's moved to the end.
        If the cache is at capacity, the least recently used item (first item)
        is removed.

        Args:
            key: The key for the item.
            value: The value to store.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

    def __repr__(self):
        return f"LRUCache(capacity={self.capacity}, items={list(self.cache.items())})"

def demo():
    """
    Demonstrate the functionality of the LRUCache class.
    """
    print("Initializing LRU Cache with capacity 2...")
    lru = LRUCache(2)

    print("Putting (1, 'one')...")
    lru.put(1, "one")
    print("Putting (2, 'two')...")
    lru.put(2, "two")
    print(f"Current Cache: {lru}")

    print(f"Getting key 1: {lru.get(1)}")
    print("Cache after getting 1 (1 should be most recent):")
    print(lru)

    print("Putting (3, 'three')... (This should evict key 2)")
    lru.put(3, "three")
    print(f"Current Cache: {lru}")

    print(f"Getting key 2 (should be None): {lru.get(2)}")

if __name__ == "__main__":
    demo()
