#!/usr/bin/env python3
"""A Basic python async function"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    max_delay = uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return max_delay
