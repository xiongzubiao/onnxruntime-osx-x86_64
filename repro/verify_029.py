"""
LRU Cache Implementation using collections.OrderedDict.

This module provides a Least Recently Used (LRU) cache class that maintains
a fixed capacity and evicts the least recently used items when the limit is reached.
"""

from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache implementation.

    Attributes:
        capacity (int): Maximum number of items the cache can hold.
        cache (OrderedDict): Internal storage for cache items.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a specific capacity.

        Args:
            capacity (int): The maximum size of the cache.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Retrieve an item from the cache.

        Moves the accessed item to the end to mark it as most recently used.

        Args:
            key (int): The key to retrieve.

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

        If the cache exceeds capacity, the least recently used item is evicted.

        Args:
            key (int): The key to insert or update.
            value (int): The value to store.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

def run_demo():
    """
    Demonstrate the LRU cache functionality.
    """
    print("Initializing LRU Cache with capacity 2...")
    lru = LRUCache(2)

    print("Putting (1, 1)...")
    lru.put(1, 1)
    print("Putting (2, 2)...")
    lru.put(2, 2)
    
    print(f"Get 1: {lru.get(1)} (Expected: 1)")
    
    print("Putting (3, 3) - This should evict key 2...")
    lru.put(3, 3)
    
    print(f"Get 2: {lru.get(2)} (Expected: -1)")
    
    print("Putting (4, 4) - This should evict key 1...")
    lru.put(4, 4)
    
    print(f"Get 1: {lru.get(1)} (Expected: -1)")
    print(f"Get 3: {lru.get(3)} (Expected: 3)")
    print(f"Get 4: {lru.get(4)} (Expected: 4)")

if __name__ == '__main__':
    run_demo()
