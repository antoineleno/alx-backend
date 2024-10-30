#!/usr/bin/python3
""" Base cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""
    def put(self, key, item):
        """Add an iems to the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
        else:
            return

    def get(self, key):
        """Get an item by key from the cache"""
        self.cache_data.get(key, None)
