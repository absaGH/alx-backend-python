#!/usr/bin/env python3
""" Based on task one; it takes in 2 int arguments:
    max_delay and n. it will spawn wait_random n times with the specified
    max_delay and return the list of all the delays in ascending order.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ execute max_delay n times  """
    delays: List[float] = []
    delays_list: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        delays_list.append(earliest_result)
    return delays_list
