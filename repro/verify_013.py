"""
Reproduction script for verifying LRU cache functionality using OrderedDict.
"""

from collections import OrderedDict

class LRUCache:
    """
    A simple Least Recently Used (LRU) Cache implementation using OrderedDict.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a fixed capacity.

        Args:
            capacity (int): Maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.
        Moves the accessed item to the end (most recent).

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
        Set or insert the value if the key is not already present. 
        When the cache reaches its capacity, it should invalidate the least recently used item 
        before inserting a new item.

        Args:
            key (int): The key to insert or update.
            value (int): The value to associate with the key.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    print("Testing LRUCache...")
    lru = LRUCache(2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"get(1): {lru.get(1)}")  # returns 1
    
    lru.put(3, 3)    # evicts key 2
    print(f"get(2): {lru.get(2)}")  # returns -1 (not found)
    
    lru.put(4, 4)    # evicts key 1
    print(f"get(1): {lru.get(1)}")  # returns -1 (not found)
    print(f"get(3): {lru.get(3)}")  # returns 3
    print(f"get(4): {lru.get(4)}")  # returns 4
    print("Demo completed.")
