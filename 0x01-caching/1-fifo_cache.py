#!/usr/bin/env python3
"""
    FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import deque
from typing import Any


class FIFOCache(BaseCaching):
    def __init__(self) -> None:
        """
            Initialiaze the class
        """
        super().__init__()
        self.__queue = deque()

    def put(self, key, item) -> None:
        """
            Must assign to the dictionary self.cache_data
            the item value for the key key
        """
        if len(self.cache_data) == self.MAX_ITEMS:
            key_discard = self.__queue.popleft()
            self.cache_data.pop(key_discard)
            print(f"DISCARD: {key_discard}")
        if key and item:
            self.cache_data.__setitem__(key, item)
            self.__queue.append(key)

    def get(self, key) -> Any:
        """
            Must return the value in self.cache_data linked to key
        """
        if key:
            return self.cache_data.get(key, None)
        return None
