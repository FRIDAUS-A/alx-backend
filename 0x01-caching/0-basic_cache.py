#!/usr/bin/env python3
"""
    BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    """
        Basic Cache class
    """
    def __init__(self) -> None:
        """
            initialize base caching
        """
        super().__init__()

    def put(self, key, item) -> None:
        """
            Must assign to the dictionary self.cache_data
            the item value for the key key.
        """
        if key and item:
            self.cache_data.__setitem__(key, item)

    def get(self, key) -> Any:
        """
            Must return the value in self.cache_data linked to key.
        """
        if key:
            return self.cache_data.get(key, None)
        return None
