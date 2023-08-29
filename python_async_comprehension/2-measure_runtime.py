#!/usr/bin/env python3
"""Async comprehension"""
import asyncio
from typing import List

# Importez la fonction async_comprehension du fichier précédent
async_comprehension = __import__('1-async_comprehension').async_comprehension

# Définissez la coroutine measure_runtime
async def measure_runtime() -> List[float]:
    "async gather 4 fois"
    start_time = time.time()
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    total_time = end_time - start_time
    return total_time

