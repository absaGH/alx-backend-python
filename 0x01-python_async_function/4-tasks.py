#!/usr/bin/env python3
""" A modification of wait_n code. """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n function that uses task_wait_random  """
    delays: List[float] = []
    delays_list: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        delays_list.append(earliest_result)
    return delays_list
