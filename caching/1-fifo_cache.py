#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a caching system using the FIFO algorithm
    """

    def __init__(self):
        """ Initialize """
        # Call the parent class constructor
        super().__init__()
        # List to keep track of the order of items
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        # Add item to the cache
        self.cache_data[key] = item
        if key not in self.keys:
            # Add key to the keys list
            self.keys.append(key)

        # Check if the number of items exceeds the limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the oldest item from the list
            discard = self.keys.pop(0)
            # Remove the oldest item from the cache
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
