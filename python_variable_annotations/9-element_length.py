#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a float """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    "Return list of tuple and int"
    return [(i, len(i)) for i in lst]
