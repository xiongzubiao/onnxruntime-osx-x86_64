"""
LRU Cache implementation using collections.OrderedDict.
"""

from collections import OrderedDict

class LRUCache:
    """
    A simple LRU (Least Recently Used) cache implementation.
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
        
        Args:
            key: The key to look up.
            
        Returns:
            The value associated with the key, or -1 if the key is not present.
        """
        if key not in self.cache:
            return -1
        # Move the accessed item to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Insert or update an item in the cache.
        
        Args:
            key: The key for the item.
            value: The value for the item.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

if __name__ == "__main__":
    # Demo of the LRU cache
    print("Initializing LRU cache with capacity 2...")
    cache = LRUCache(2)

    print("Putting (1, 1)...")
    cache.put(1, 1)
    print("Putting (2, 2)...")
    cache.put(2, 2)
    
    print(f"Get 1: {cache.get(1)}")  # returns 1
    
    print("Putting (3, 3)... evicts key 2")
    cache.put(3, 3)
    
    print(f"Get 2: {cache.get(2)}")  # returns -1 (not found)
    
    print("Putting (4, 4)... evicts key 1")
    cache.put(4, 4)
    
    print(f"Get 1: {cache.get(1)}")  # returns -1 (not found)
    print(f"Get 3: {cache.get(3)}")  # returns 3
    print(f"Get 4: {cache.get(4)}")  # returns 4
