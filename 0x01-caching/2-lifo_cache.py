#!/usr/bin/env python3
"""LIFO caching module.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching
    and is a caching system for last in and First out
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
            last_value = list(self.cache_data.keys())[-2]
            print("DISCARD: {}".format(last_value))
            del self.cache_data[last_value]

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
