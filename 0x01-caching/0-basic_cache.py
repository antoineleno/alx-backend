#!/usr/bin/python3
""" Base cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class that allow to store and get an item"""
    def put(self, key, item):
        """Add an iems to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key from the cache"""
        self.cache_data.get(key, None)


