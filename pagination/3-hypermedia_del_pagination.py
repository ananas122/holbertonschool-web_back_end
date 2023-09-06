#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dict with hyper pagination info based on index"""
        # Vérifie si l'index est dans la plage valide
        assert index is None or 0 <= index < len(self.indexed_dataset())

        # Vérifie que page_size est un int positif
        assert type(page_size) == int and page_size > 0

        # Calcule l'index de départ de la page current
        current_index = index if index is not None else 0
        # Calcule l'index de début de la prochaine page
        next_index = current_index + page_size

        # Obtient l'ensemble des données indexées
        indexed_data = self.indexed_dataset()
        # Initialise une liste pour stocker les données de la page
        data = []

        i = current_index
        while i < next_index and i < len(indexed_data):
            # ajoute les données à la liste
            data.append(indexed_data.get(i, []))
            i += 1

        # Retourne un dict contenant les info de pagination
        return {
            "index": current_index,
            "next_index":
                next_index if next_index < len(indexed_data) else None,
            "page_size": page_size,
            "data": data
        }
