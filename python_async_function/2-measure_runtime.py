#!/usr/bin/env python3
"""Mesure time"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    "Mesure time"
    # Start measuring the execution time
    start_time = time.time()

    # Run the wait_n function asynchronously
    asyncio.run(wait_n(n, max_delay))

    # Stop measuring the execution time
    end_time = time.time()

    # Calculate the total time by subtracting the start time from the end time
    total_time = end_time - start_time

    # Return the average time
    return total_time / n
