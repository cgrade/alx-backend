#!/usr/bin/env python3
""" A module that contains a class that inheretied from
    the base Caching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
                key (_type_): _description_
                item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
    """ A class that inherit from the BaseCaching Class
        with it's own implementations.
    """
    MAX_ITEMS = None

    def __init__(self) -> None:
        super().__init__()

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
