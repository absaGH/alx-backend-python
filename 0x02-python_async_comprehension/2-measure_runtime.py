#!/usr/bin/env python3
""" Based on Task-1, it creates measure_runtime coroutine that
    will execute async_comprehension four times
    in parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time of four parallel comprehensions """
    tasks = []
    start = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
