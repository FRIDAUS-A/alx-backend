#!/usr/bin/env python3
"""
    a function named index_range that takes two integer
    arguments page and page_size.
"""
from typing import Tuple


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
