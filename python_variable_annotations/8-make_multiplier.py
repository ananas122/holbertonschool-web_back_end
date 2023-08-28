#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a float """
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return  a float multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
