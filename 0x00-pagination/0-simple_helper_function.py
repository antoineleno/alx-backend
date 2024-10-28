#!/usr/bin/env python3
"""0-simple helper function module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Index range function"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
