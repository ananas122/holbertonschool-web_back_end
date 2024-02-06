#!/usr/bin/env python3
""" LIFOCache module """
# Import the base caching class BaseCaching
from base_caching import BaseCaching

# Define a new class LIFOCache that inherits from BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a caching system using the LIFO algorithm
    """

    # The constructor of the class
    def __init__(self):
        """ Initialize """
        # Call the parent class constructor
        super().__init__()
        # Create a list to keep track of the order of items.
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    # Remove the last item from the cache (LIFO)
                    del self.cache_data[self.keys[-1]]
                    print("DISCARD:", self.keys[-1])
                    self.keys.pop(-1)
            # Add the item to the cache and to the keys list
            self.cache_data[key] = item
            self.keys.append(key)

    # Method to get an item by key
    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
