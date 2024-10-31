#!/usr/bin/env python3
"""
    a class LFUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from typing import Any
from collections import deque


class LFUCache(BaseCaching):
    """
        Least Frequently used class
    """
    def __init__(self):
        """
            Initialize class
        """
        super().__init__()
        self.__lfu = {}
        self.__lru = deque()

    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data
            the item value for the key key
        """
        if key and item:
            if self.cache_data.__len__() ==\
               self.MAX_ITEMS and key not in self.__lru:
                key_discard = min(self.__lfu, key=self.__lfu.get)
                value_discard = self.__lfu[key_discard]
                keys_to_discard = []
                lfu_copy = self.__lfu.copy()  # create a copy
                while lfu_copy:
                    key_discard = min(lfu_copy, key=lfu_copy.get)
                    if lfu_copy[key_discard] == value_discard:
                        keys_to_discard.append(key_discard)
                    value = lfu_copy[key_discard]
                    lfu_copy.pop(key_discard)
                if len(keys_to_discard) == 1:
                    key_discard = keys_to_discard[0]
                else:
                    lru = self.__lru.copy()
                    while lru:
                        key_discard = lru.popleft()
                        if key_discard in keys_to_discard:
                            break
                self.cache_data.pop(key_discard)
                self.__lfu.pop(key_discard)
                print(f"DISCARD: {key_discard}")
            if key in self.__lru:
                self.__lru.remove(key)
            self.__lru.append(key)
            self.cache_data.__setitem__(key, item)
            self.__lfu[key] = 1 + self.__lfu.get(key, 0)

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key
        """
        if key and (key in self.cache_data):
            try:
                self.__lru.remove(key)
            except ValueError:
                pass
            self.__lru.append(key)
            self.__lfu[key] = 1 + self.__lfu.get(key, 0)
            return self.cache_data.get(key, None)
        return None
