#!/usr/bin/env python3
"""type-annotated func to_kv that takes a string k and an int OR float v as arguments and returns a tuple."""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with string k and the square of int/float v."""
    return k, v ** 2
