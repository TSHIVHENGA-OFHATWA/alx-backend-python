#!/usr/bin/env python3
"""
This module contains an async routine to execute
multiple coroutines concurrently.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    and return list of delays.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
