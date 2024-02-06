#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a caching system using the LIFO algorithm.
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.last_key_added = None  # Track the last key added

    def put(self, key, item):
        """
        Add or update an item in the cache.
        Discards the last item added if the cache exceeds its limit (LIFO algorithm).
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key_added = key  # Update the last key added

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key_added:
                print("DISCARD: {}".format(self.last_key_added))
                del self.cache_data[self.last_key_added]
                self.last_key_added = None  # Reset last_key_added

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
