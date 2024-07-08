#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

from typing import List
from asyncio import gather

# import wait_random from previous file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """run an async function n times with max_delay returning list of delays"""
    list_of_delays: float = []
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    results = await gather(*coroutines)
    list_of_delays.extend(results)

    return sorted(list_of_delays)
