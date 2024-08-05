#!/usr/bin/env python3
"""
This module contains A basic async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine that takes in an integer argument:
    Args:
        max_delay: int with default value 10.
    Description:
        This function waits for a random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    return delay
