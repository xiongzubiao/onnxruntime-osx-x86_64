"""
This module provides a simple implementation of an LRU (Least Recently Used) cache
using Python's collections.OrderedDict.
"""

from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache implementation.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a fixed capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        Retrieve an item from the cache.

        If the key exists, it is moved to the end to represent recent use.
        Returns the value if found, otherwise None.

        Args:
            key: The key to look up.
        """
        if key not in self.cache:
            return None
        # Move to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Add or update an item in the cache.

        If the key already exists, its value is updated and it's moved to the end.
        If the cache exceeds capacity, the least recently used item (first item) is removed.

        Args:
            key: The key for the item.
            value: The value for the item.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (Least Recently Used)
            self.cache.popitem(last=False)

def demo():
    """
    Demonstrates the usage of the LRUCache class.
    """
    print("Initializing LRU Cache with capacity 2...")
    lru = LRUCache(2)

    print("Putting (1, 'one')")
    lru.put(1, "one")
    print("Putting (2, 'two')")
    lru.put(2, "two")

    print(f"Get 1: {lru.get(1)}")  # Returns 'one', 1 becomes most recent

    print("Putting (3, 'three') - this should evict key 2")
    lru.put(3, "three")

    print(f"Get 2: {lru.get(2)}")  # Returns None
    print(f"Get 3: {lru.get(3)}")  # Returns 'three'

if __name__ == '__main__':
    demo()
