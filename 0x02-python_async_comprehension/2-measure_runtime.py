#!/usr/bin/env python3
"""Measure the time to run a couroutine multiple times"""

import asyncio
from time import perf_counter

async_compr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel"""
    start = perf_counter()
    await asyncio.gather(async_compr(), async_compr(), async_compr(),
                         async_compr())
    return perf_counter() - start
