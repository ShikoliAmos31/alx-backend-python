#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

from typing import List
from asyncio import gather

# import wait_random from previous file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """run an async function n times with max_delay returning list of delays"""
    list_of_delays: float = []
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await gather(*coroutines)
    list_of_delays.extend(results)

    return sorted(list_of_delays)
