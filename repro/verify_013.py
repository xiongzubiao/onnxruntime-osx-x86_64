"""
LRU Cache Implementation.

This module provides a Least Recently Used (LRU) cache implementation using
collections.OrderedDict for efficient O(1) operations.
"""

from collections import OrderedDict
from typing import Any, Optional

class LRUCache:
    """
    A simple Least Recently Used (LRU) cache.

    The cache has a fixed capacity. When the capacity is reached, the least
    recently used item is evicted to make room for new items.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.

        Args:
            capacity: Maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve an item from the cache.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if the key is not present.
        """
        if key not in self.cache:
            return None
        
        # Move the accessed item to the end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update an item in the cache.

        Args:
            key: The key to insert or update.
            value: The value to associate with the key.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # Pop the first item (least recent)
            self.cache.popitem(last=False)

    def __repr__(self) -> str:
        return f"LRUCache(capacity={self.capacity}, items={list(self.cache.keys())})"


def run_demo():
    """
    Demonstrate the functionality of the LRUCache class.
    """
    print("Initializing LRU Cache with capacity 3...")
    cache = LRUCache(3)

    print("\nPutting 1, 2, 3...")
    cache.put(1, "one")
    cache.put(2, "two")
    cache.put(3, "three")
    print(f"Current cache: {cache}")

    print("\nGetting key 1 (should move to most recent)...")
    cache.get(1)
    print(f"Current cache: {cache}")

    print("\nPutting key 4 (should evict key 2, the least recently used)...")
    cache.put(4, "four")
    print(f"Current cache: {cache}")

    print("\nChecking for key 2 (should be None):")
    print(f"Key 2: {cache.get(2)}")

    print("\nPutting key 5 (should evict key 3)...")
    cache.put(5, "five")
    print(f"Current cache: {cache}")


if __name__ == "__main__":
    run_demo()
