#!/usr/bin/env python3
"""task 0"""
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self._data = []  # Initialisez _data avec une liste vide

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
        "Verify if page and page size are int posits"
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        # Get the start and end indexes of the range
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        # Call get_page method to retrieve the dataset page
        data = self.get_page(page, page_size)

        # Calculate the number of pages based on the total rows and page size
        total_pages = math.ceil((len(self._data) - 1) / page_size)

        # Create the hyper dictionary
        return  {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }



def index_range(page: int, page_size: int) -> Tuple[int, int]:
    "return index range"
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
