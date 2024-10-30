#!/usr/bin/env python3
"""LRU caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache that inherits from BaseCaching
    and is a caching system for last in and First out
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            first_value, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(first_value))

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
