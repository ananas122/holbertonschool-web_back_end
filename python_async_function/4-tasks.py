#!/usr/bin/env python3
"""async and await syntax"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    "Define the task_wait_n function with prm n and max_delay
    # Create an empty list to store the delays
    delays = []
    # Loop n times to create and await each task
    for _ in range(n):
        # Create a task using task_wait_random with max_delay
        task = task_wait_random(max_delay)
        # Await the task and append the delays list
        delays.append(await task)
    return sorted(delays)
