"""
Module for verifying LRU Cache implementation using OrderedDict.
"""

from collections import OrderedDict

class LRUCache:
    """
    A simple Least Recently Used (LRU) Cache using collections.OrderedDict.
    """
    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache with a fixed capacity.
        
        Args:
            capacity (int): Maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieve an item from the cache. Moves the key to the end to show it was recently used.
        
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
        Insert or update an item in the cache. If the capacity is reached, 
        it removes the least recently used item.
        
        Args:
            key (int): The key to store.
            value (int): The value to associate with the key.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    print("Running LRU Cache Demo...")
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"Get 1: {lru.get(1)}")  # returns 1
    lru.put(3, 3)                  # evicts key 2
    print(f"Get 2 (should be -1): {lru.get(2)}")
    lru.put(4, 4)                  # evicts key 1
    print(f"Get 1 (should be -1): {lru.get(1)}")
    print(f"Get 3: {lru.get(3)}")  # returns 3
    print(f"Get 4: {lru.get(4)}")  # returns 4
    print("Demo completed successfully.")
