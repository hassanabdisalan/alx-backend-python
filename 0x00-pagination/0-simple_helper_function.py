#!/usr/bin/env python3
"""A helper function for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
