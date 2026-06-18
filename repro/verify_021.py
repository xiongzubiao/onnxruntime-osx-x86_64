"""
LRU Cache Implementation using OrderedDict.

This module provides a simple Least Recently Used (LRU) cache implementation
leveraging Python's collections.OrderedDict to maintain access order.
"""

from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache.

    The cache has a fixed capacity. When the capacity is reached, the least
    recently used item is removed before adding a new item.
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

        If the key exists, it is moved to the end (most recently used).
        If the key does not exist, returns -1.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or -1 if not found.
        """
        if key not in self.cache:
            return -1
        
        # Move the accessed item to the end (MRU)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Insert or update a key-value pair in the cache.

        If the key exists, it is updated and moved to the end.
        If the key is new and the cache is at capacity, the oldest item is removed.

        Args:
            key: The key to insert or update.
            value: The value to store.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # Pop the first item (LRU)
            self.cache.popitem(last=False)

    def __repr__(self):
        return f"LRUCache(capacity={self.capacity}, items={list(self.cache.items())})"

if __name__ == "__main__":
    print("--- LRU Cache Demo ---")
    
    # Initialize cache with capacity of 2
    lru = LRUCache(2)
    
    print(f"Initial state: {lru}")
    
    print("\nPutting (1, 'A') and (2, 'B')...")
    lru.put(1, "A")
    lru.put(2, "B")
    print(f"Current state: {lru}")
    
    print(f"\nGetting key 1: {lru.get(1)} (should be 'A')")
    print(f"State after getting 1 (1 should be MRU): {lru}")
    
    print("\nPutting (3, 'C') (capacity reached, 2 should be evicted)...")
    lru.put(3, "C")
    print(f"Current state: {lru}")
    
    print(f"\nGetting key 2: {lru.get(2)} (should be -1)")
    print(f"Getting key 1: {lru.get(1)} (should be 'A')")
    
    print("\nPutting (4, 'D') (capacity reached, 3 should be evicted)...")
    lru.put(4, "D")
    print(f"Final state: {lru}")
