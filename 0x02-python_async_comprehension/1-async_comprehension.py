#!/usr/bin/env python3
""" Based on task-0, it creates coroutine that will collect
    10 random numbers using an async comprehensing. """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async Comprehensions """
    return [i async for i in async_generator()]
