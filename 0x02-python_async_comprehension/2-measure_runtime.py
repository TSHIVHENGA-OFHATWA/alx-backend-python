#!/usr/bin/env python3
"""
Module for measuring the runtime of running async_comprehension.
"""

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of execution and return it"""
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start_time
