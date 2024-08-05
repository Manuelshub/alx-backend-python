#!/usr/bin/env python3
"""
This module contains a function called task_wait_n
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a specified number of tasks to
    complete and returns the random delays for each task.

    Args:
        n (int): The number of tasks to wait for.
        max_delay (int): The maximum delay for each task.

    Returns:
        list: A list of the random delays for each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
