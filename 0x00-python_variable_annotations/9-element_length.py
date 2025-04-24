#!/usr/bin/env python3
"""Annotate function parameters and return value"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuples containing each sequence and its length"""
    return [(i, len(i)) for i in lst]
