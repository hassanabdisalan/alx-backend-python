#!/usr/bin/env python3
"""Module that defines an asynchronous comprehension to collect random numbers."""

from typing import List
from . import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension over async_generator,
    and return them.
    """
    return [i async for i in async_generator()]
