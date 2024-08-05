#!/usr/bin/env python3
"""
This module contains a Coroutine
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Asynchronously wait for a number of coroutines to complete.

    Args:
        n (int): The number of coroutines to wait for.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        list: A list of the random delays for each coroutine.
    """
    lst = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        i = 0
        while i < len(lst) and lst[i] < delay:
            i += 1
        lst.insert(i, delay)
    return lst
