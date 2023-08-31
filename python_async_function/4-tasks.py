#!/usr/bin/env python3
"""async and await syntax"""
import asyncio
from typing import List


wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    "Waits for 'n' tasks to complete 'max_delay"
    # Create a list of tasks, each task executing the max_delay
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Use asyncio.gather to wait for all tasks to complete
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
