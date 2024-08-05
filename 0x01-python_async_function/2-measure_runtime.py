#!/usr/bin/env python3
"""
This module contains an asynchronous function that measures
the total execution time of a function
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of the `wait_n` coroutine.

    Args:
        n (int): The number of coroutines to wait for.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average runtime of the `wait_n` coroutine in seconds.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
