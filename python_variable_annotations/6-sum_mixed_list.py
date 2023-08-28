#!/usr/bin/env python3
"""type-annotated func sum_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "Return the sum of the input list"
    return sum(mxd_lst)
