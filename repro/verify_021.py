"""
LRU Cache Implementation using collections.OrderedDict.

This module provides a Least Recently Used (LRU) cache class that maintains
a fixed capacity and evicts the least recently used items when the limit is reached.
"""

from collections import OrderedDict
from typing import Any, Optional


class LRUCache:
    """
    A Least Recently Used (LRU) cache.

    The cache has a fixed capacity and will remove the oldest item
    (least recently used) when new items are added beyond its capacity.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve an item from the cache.

        Args:
            key (Any): The key of the item to retrieve.

        Returns:
            Any: The value associated with the key, or None if not found.
        """
        if key not in self.cache:
            return None
        # Move the accessed item to the end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: Any, value: Any) -> None:
        """
        Add or update an item in the cache.

        If the cache exceeds its capacity, the least recently used item is evicted.

        Args:
            key (Any): The key for the item.
            value (Any): The value for the item.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

    def __repr__(self) -> str:
        return f"LRUCache(capacity={self.capacity}, items={list(self.cache.keys())})"


def main():
    """
    Demonstration of the LRUCache implementation.
    """
    print("Initializing LRU Cache with capacity 2...")
    cache = LRUCache(2)

    print("Putting {1: 1}, {2: 2}")
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"Cache state: {cache}")

    print(f"Getting key 1: {cache.get(1)}")  # returns 1
    print(f"Cache state after getting 1: {cache}")

    print("Putting {3: 3} (should evict key 2)")
    cache.put(3, 3)
    print(f"Cache state: {cache}")

    print(f"Getting key 2: {cache.get(2)}")  # returns None (evicted)
    print(f"Getting key 1: {cache.get(1)}")  # returns 1
    print(f"Getting key 3: {cache.get(3)}")  # returns 3


if __name__ == "__main__":
    main()
