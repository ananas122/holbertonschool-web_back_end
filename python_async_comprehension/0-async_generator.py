#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments."""
import asyncio
import random


async def async_generator():
    "An asynchronous generator that yields float values."
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
