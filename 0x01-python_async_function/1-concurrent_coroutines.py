#!/usr/bin/env python3
"""execute multiple coroutines at the same time"""

import asyncio
from typing import List
from heapq import heappush, heappop


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified
    max_delay and returns the list of all delays"""
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        heappush(delays, delay)

    return [heappop(delays) for _ in range(len(delays))]
