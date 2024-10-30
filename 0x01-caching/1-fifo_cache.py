#!/usr/bin/env python3
"""FIFO caching module.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache that inherits from BaseCaching
    and is a caching system for first in and frist out
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_value = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(first_value))
            del self.cache_data[first_value]
        

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
