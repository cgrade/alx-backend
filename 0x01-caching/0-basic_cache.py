#!/usr/bin/env python3
""" A module that contains a class that inheretied from
    the base Caching class
"""


class BaseCaching():
    """ BaseCahing defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self) -> None:
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self) -> None:
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


class BasicCache(BaseCaching):
    """ A class that inhereit from the BaseCaching Class
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
