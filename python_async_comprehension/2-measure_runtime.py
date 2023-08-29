#!/usr/bin/env python3
"""Définissez la coroutine measure_runtime"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    "async gather 4 fois"
    start_time = time.time()
    # Créez une liste pour stocker les futures des exécutions async_comprehension
    tasks = [async_comprehension() for _ in range(4)]
    # Exécutez les coroutines
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
