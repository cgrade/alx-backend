#!/usr/bin/env python3
""" A module that contains a class that inhereited form the base class
    for LIFO caching policy
"""
from basic import base_caching


class LIFOCache(base_caching.BaseCaching):
    """ FIFO Class that inherits from a Base Class
    """
    def __init__(self):
        """ Initialization
        """
        super().__init__()

    def put(self, key, item):
        """ A method that insert data into the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(list(self.cache_data)) >= self.MAX_ITEMS and key not in \
                   self.cache_data.keys():
                last_item = list(self.cache_data)[self.MAX_ITEMS - 1]
                print(f'DISCARD: {last_item}')
                self.cache_data.popitem()
            self.cache_data[key] = item

    def get(self, key):
        """ A method that returns the given key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
