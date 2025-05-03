#!/usr/bin/env python3

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
async def measure_runtime() -> float:
    """
    Coroutine that runs async_comprehension four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.
    
    Returns:
        float: The total time it took to run async_comprehension four times.
    """
    start_time = time.time()  # Record the start time
    
    # Run async_comprehension 4 times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.time()  # Record the end time
    
    return end_time - start_time  # Return the total time taken
