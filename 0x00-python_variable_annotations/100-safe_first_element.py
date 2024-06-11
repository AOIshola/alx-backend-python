#!/usr/bin/env python3
"""Duck-Typed annotations"""

from typing import Any, Sequence, Union, TypeVar


T = TypeVar('T')
NoneType = TypeVar('NoneType', bound=None)


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """return first element"""
    if lst:
        return lst[0]
    else:
        return None
