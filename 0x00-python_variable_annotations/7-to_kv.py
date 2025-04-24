#!/usr/bin/env python3
"""Defines a function that returns a tuple with a string and the square of a number"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is a string `k`,
    and the second is the square of `v` as a float"""
    return (k, float(v ** 2))
