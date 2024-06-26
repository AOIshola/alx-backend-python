#!/usr/bin/env python3
"""Creates a python async generator"""

import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """generates and yields a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
