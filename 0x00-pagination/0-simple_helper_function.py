#!/usr/bin/env python3
"""0-simple helper function module"""


def index_range(page: int, page_size: int) -> tuple:
    """Index range function"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
