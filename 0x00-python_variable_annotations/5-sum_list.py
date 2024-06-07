#!/usr/bin/env python3
"""A type-annotated sum_list python function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """adds all items in a list"""
    return sum(input_list)
