#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    "The basics of async"
    # Generate a random delay within the given max_delay
    delay = random.uniform(0, max_delay)
    # Asynchronously sleep for the generated delay
    await asyncio.sleep(delay)
    return delay
