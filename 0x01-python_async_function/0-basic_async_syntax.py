#!/usr/bin/env python3
"""
This module contains A basic async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    delay = random.uniform(0, max_delay)
    return delay
