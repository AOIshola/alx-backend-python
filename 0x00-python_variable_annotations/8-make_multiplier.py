#!/usr/bin/env python3
"""A type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a multiplier"""
    def result(number: float) -> float:
        """function multiplying float and multiplier"""
        return number * multiplier
    return result
