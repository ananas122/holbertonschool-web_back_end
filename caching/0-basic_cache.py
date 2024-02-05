#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ 
    BasicCache caching system.

    This class represents a basic caching system that inherits from BaseCaching.
    It uses a dictionary to store data without any size limit.
    """

    def put(self, key, item):
        """
        Add or update an item in the cache.

        Args:
            key: The key for the item to be added or updated.
            item: The value of the item.
        """
        # Add the item only if neither the key nor the value is None
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by its key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key in the cache, or None if the key
            is absent or None.
        """
        # Return the value associated with the key if it exists in the cache
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
