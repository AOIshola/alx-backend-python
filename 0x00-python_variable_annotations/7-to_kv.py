#!/usr/bin/env python3
"""type-annotated function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of key-value pairs"""
    return (k, v ** 2)
