#!/usr/bin/env python3
"""
This module contains A basic async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay:
    Args:
        max_delay(int): Maximum delay with default value 10.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
