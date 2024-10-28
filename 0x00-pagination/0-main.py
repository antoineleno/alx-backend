#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)


            """Retrieves info about a page from a given index and with a
            specified size.
            """
            data = self.indexed_dataset()
            assert index is not None and index >= 0 and index <= max(data.keys())
            page_data = []
            data_count = 0
            next_index = None
            start = index if index else 0
            for i, item in data.items():
                if i >= start and data_count < page_size:
                    page_data.append(item)
                    data_count += 1
                    continue
                if data_count == page_size:
                    next_index = i
                    break
            my_dict = {
                'index': index,
                'next_index': next_index,
                'page_size': len(page_data),
                'data': page_data,
            }
            return my_dict