"""
LRU Cache Implementation module.

This module provides a Least Recently Used (LRU) cache implementation using
collections.OrderedDict for efficient O(1) operations.
"""

from collections import OrderedDict
from typing import Any, Optional

class LRUCache:
    """
    A simple LRU Cache implementation with fixed capacity.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve an item from the cache.

        Args:
            key (Any): The key to look up.

        Returns:
            Optional[Any]: The value associated with the key, or None if not found.
        """
        if key not in self.cache:
            return None
        # Move the accessed key to the end to mark it as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: Any, value: Any) -> None:
        """
        Add or update an item in the cache.

        Args:
            key (Any): The key to add/update.
            value (Any): The value to store.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

def main():
    """
    Demonstration of the LRUCache functionality.
    """
    print("Initializing LRU Cache with capacity 2...")
    cache = LRUCache(2)

    print("Putting (1, 'one')...")
    cache.put(1, "one")
    print("Putting (2, 'two')...")
    cache.put(2, "two")

    print(f"Get 1: {cache.get(1)}")  # Returns \"one\"

    print("Putting (3, 'three') - this should evict key 2...")
    cache.put(3, "three")

    print(f"Get 2 (should be None): {cache.get(2)}")
    print(f"Get 1 (should be 'one'): {cache.get(1)}")
    print(f"Get 3 (should be 'three'): {cache.get(3)}")

if __name__ == "__main__":
    main()
