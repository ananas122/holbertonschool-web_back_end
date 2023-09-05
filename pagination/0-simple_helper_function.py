#!/usr/bin/env python3
""" task 0 """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    "return index range"
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
