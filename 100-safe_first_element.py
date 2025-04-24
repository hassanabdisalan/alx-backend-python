#!/usr/bin/env python3
"""Duck-typed annotated function"""

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence or None if it's empty"""
    if lst:
        return lst[0]
    else:
        return None
