#!/usr/bin/env python3
"""
    a class LRUCache that inherits from BaseCaching and is a caching system
"""
from collections import deque
from base_caching import BaseCaching
from typing import Any


class LRUCache(BaseCaching):
    """
        LRUCache class
    """
    def __init__(self):
        """
            Initialize class
        """
        super().__init__()
        self.__lru = deque()  # least recently used

    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data
            the item value for the key key
        """
        if self.cache_data.__len__() == \
           self.MAX_ITEMS and key not in self.__lru:
            key_discard = self.__lru.popleft()
            self.cache_data.pop(key_discard)
            print(f"DISCARD: {key_discard}")
        if key and item:
            if key in self.__lru:
                self.__lru.remove(key)
            self.cache_data.__setitem__(key, item)
            self.__lru.append(key)

    def get(self, key) -> Any:
        """
            Must return the value in self.cache_data linked to key
        """
        if key:
            try:
                self.__lru.remove(key)
                self.__lru.append(key)
            except ValueError:
                pass
            return self.cache_data.get(key, None)
        return None
