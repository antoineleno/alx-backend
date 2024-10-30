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
            pass

    def get(self, key):
        """Get an item by key from the cache"""
        if key is None:
            return None

        for key in self.cache_data:
            if key == key:
                return self.cache_data[key]
            else:
                return None
