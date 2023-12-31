#!/usr/bin/env python3
"""type-annotated func sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    "Return the sum of the input list"
    return sum(input_list)
