#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Invoke wait_random n times with the specified max_delay."""
    # Create an empty list to store the delays
    delays = []
    # Repeat the following process 'n' times
    for _ in range(n):
        # Call the wait_random function and await its result
        delay = await wait_random(max_delay)
        # Append the delay to the list of delays
        delays.append(delay)
    # Sort the list of delays in ascending order
    return sorted(delays)


