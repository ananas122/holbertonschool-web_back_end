#!/usr/bin/env python3
"""LRU module """
# Import the base caching class BaseCaching
from base_caching import BaseCaching


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system using the (LRU) algorithm
    """

    def __init__(self):
        """ Initialize the LRU cache """
        super().__init__()
        # Create a list to keep track of the order of keys
        self.lru_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find and remove the least recently used item
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add the new item to the cache and update the LRU order
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the LRU order
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
