#!/usr/bin/env python3
""" coroutine that will loop 10 times, each time asynchronously wait 1 second.
    And then it yield a random number between 0 and 10. Use the random module.
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ Asynchronous Generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
