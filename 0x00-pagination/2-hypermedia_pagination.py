#!/usr/bin/env python3
"""
Simple pagination module
"""
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Index range helper function that return a tuple
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        """GEt page method
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        if start > len(self.dataset()):
            return []
        else:
            return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Hypermedia pagination method
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if end < len(self.__dataset) else None
        prev_page = page - 1 if start > 0 else None
        my_dict = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
        return my_dict
