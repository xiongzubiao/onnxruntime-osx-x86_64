"""
LRU Cache Implementation using OrderedDict.

This module provides a simple Least Recently Used (LRU) cache implementation
that leverages the features of Python's collections.OrderedDict.
"""

from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache.

    The cache has a fixed capacity and discards the least recently used
    items when the capacity is reached.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a specific capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Retrieve an item from the cache.

        If the key exists, it is moved to the end to represent recent access.
        If the key does not exist, returns -1.

        Args:
            key (int): The key to look up.

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

        If the key exists, its value is updated and it's moved to the end.
        If the cache exceeds capacity, the oldest item is removed.

        Args:
            key (int): The key to store.
            value (int): The value to store.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    # Demo of LRUCache
    print("Initializing LRU Cache with capacity 2")
    cache = LRUCache(2)

    print("Putting (1, 1)")
    cache.put(1, 1)
    print("Putting (2, 2)")
    cache.put(2, 2)

    print(f"Getting key 1: {cache.get(1)}")  # returns 1

    print("Putting (3, 3) - this should evict key 2")
    cache.put(3, 3)

    print(f"Getting key 2: {cache.get(2)}")  # returns -1 (evicted)
    print(f"Getting key 1: {cache.get(1)}")  # returns 1
    print(f"Getting key 3: {cache.get(3)}")  # returns 3
