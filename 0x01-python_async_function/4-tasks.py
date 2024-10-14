#!/usr/bin/env python3
"""
This module provides a function that runs multiple task_wait_random coroutines.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and return list of delays.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
