"""
LRU Cache Implementation using OrderedDict.

This module provides a simple Least Recently Used (LRU) cache implementation
leveraging the properties of collections.OrderedDict for efficient operations.
"""

from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache.

    The cache has a fixed capacity. When the capacity is reached and a new
    item is added, the least recently used item is discarded.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        Retrieve an item from the cache.

        Moves the retrieved item to the end (most recently used).
        Returns None if the key is not found.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None.
        """
        if key not in self.cache:
            return None
        # Move to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Add or update an item in the cache.

        If the key already exists, its value is updated and it's marked as MRU.
        If the cache is at capacity, the LRU item is removed before adding.

        Args:
            key: The key of the item.
            value: The value to store.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # popitem(last=False) removes the first item (LRU)
            self.cache.popitem(last=False)

    def __repr__(self):
        return f"LRUCache(capacity={self.capacity}, items={list(self.cache.items())})"

if __name__ == "__main__":
    print("--- LRU Cache Demo ---")
    lru = LRUCache(2)
    
    print(f"Initial: {lru}")
    
    lru.put(1, \"one\")
    lru.put(2, \"two\")
    print(f"After adding 1 and 2: {lru}")
    
    print(f"Get(1): {lru.get(1)}")
    print(f"Cache after Get(1): {lru}")
    
    lru.put(3, \"three\")
    print(f"After adding 3 (capacity 2, so 2 is evicted): {lru}")
    
    print(f"Get(2): {lru.get(2)} (should be None)")
    
    lru.put(4, \"four\")
    print(f"After adding 4 (1 is evicted): {lru}")
