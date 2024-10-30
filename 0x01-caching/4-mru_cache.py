#!/usr/bin/env python3
"""
     a class MRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from typing import Any


class MRUCache(BaseCaching):
    """
        Most Recently Used Caching Implementation
    """
    def __init__(self):
        """
            Initialize class
        """
        super().__init__()
        self.__mru = []

    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data
            the item value for the key key
        """
        if self.cache_data.__len__() == \
           self.MAX_ITEMS and key not in self.__mru:
            discard_key = self.__mru.pop()
            self.cache_data.pop(discard_key)
            print(f"DISCARD: {discard_key}")
        if key and item:
            if key in self.__mru:
                self.__mru.remove(key)
            self.cache_data.__setitem__(key, item)
            self.__mru.append(key)

    def get(self, key) -> Any:
        if key:
            try:
                self.__mru.remove(key)
                self.__mru.append(key)
            except ValueError:
                pass
            return self.cache_data.get(key, None)
        return None
