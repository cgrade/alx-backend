#!/usr/bin/env python3
"""
A module that contains  class that inherited from a base class
`BaseCaching
"""

from basic import base_caching


class FIFOCache(base_caching.BaseCaching):
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
                first_item = list(self.cache_data)[0]
                print(f'DISCARD: {first_item}')
                self.cache_data.pop(first_item)
            self.cache_data[key] = item

    def get(self, key):
        """ A method that returns the given key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
