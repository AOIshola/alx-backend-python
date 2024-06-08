#!/usr/bin/env python3
"""Type-annotated sum_mixed_list python function"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns the sum of a list"""
    return sum(mxd_list)
