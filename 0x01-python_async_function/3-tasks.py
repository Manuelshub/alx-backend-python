#!/usr/bin/env python3
"""
This module contains a function that returns asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task that waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay for the task.

    Returns:
        Task: A task object that can be awaited.
    """
    return asyncio.create_task(wait_random(max_delay))
