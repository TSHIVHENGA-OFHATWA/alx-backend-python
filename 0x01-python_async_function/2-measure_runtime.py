#!/usr/bin/env python3
"""
This module measures the runtime of the wait_n coroutine.
"""

import asyncio
import time
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for
    wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
