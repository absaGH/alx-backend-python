#!/usr/bin/env python3
""" The basics of async  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that takes in an integer argument
        and delay random amount of time in second between 0 and max_delay
        and eventually returns it.  """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
