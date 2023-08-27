#!/usr/bin/env python3
""" A module that contains a class that inheretied from
    the base Caching class
"""

BaseCaching = __import__('base_caching.py').BaseCaching


class BasicCache(BaseCaching):
    """ A class that inhereit from the BaseCaching Class
        with it's own implementations.
    """
    MAX_ITEMS = None

    def put(self, key, item):
        """ A methoed that add data into the cache
        """
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """ A method that get a data from the cache
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
