#!/usr/bin/env python3
"""Async comprehension"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    "Returns list of random float numbers."
    result = []
    async for i in async_generator():
        result.append(i)
    return result
