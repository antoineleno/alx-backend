#!/usr/bin/env python3
"""Pagination helper module.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Index range helper function that return a tuple
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
