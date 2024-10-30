#!/usr/bin/env python3
"""
    a class LIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from typing import Any


class LIFOCache(BaseCaching):
    """
        LIFO Cache Class
    """
    def __init__(self) -> None:
        super().__init__()
        self.__stack = []

    def put(self, key, item) -> None:
        """
            Must assign to the dictionary self.cache_data
            the item value for the key key
        """
        if self.cache_data.__len__() == self.MAX_ITEMS:
            key_discard = self.__stack.pop()
            self.cache_data.pop(key_discard)
            print(f"DISCARD: {key_discard}")
        if key and item:
            self.cache_data.__setitem__(key, item)
            self.__stack.append(key)

    def get(self, key) -> Any:
        """
            Must return the value in self.cache_data linked to key
        """
        if key:
            return self.cache_data.get(key, None)
        return None
