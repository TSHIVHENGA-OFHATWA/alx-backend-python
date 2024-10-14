#!/usr/bin/env python3
"""
This module provides a function to create an asyncio Task for wait_random.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task of wait_random with max_delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))
