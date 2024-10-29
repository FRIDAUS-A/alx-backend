#!/usr/bin/env python3
"""
    Implement a method named get_page that takes two integer arguments
    page with default value 1 and page_size with default value 10.
"""
import csv
from typing import Tuple, List
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Args:
            page: the current_page
            page_size: the size f the current page
        Return:
            returns a tuple containing the start
            and end of the page
    """
    return (page * page_size - page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            get page by index
        """
        if type(page) is int:
            assert page > 0
        if type(page_size) is int:
            assert page_size > 0
        assert type(page) is int
        assert type(page_size) is int
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start: end]
