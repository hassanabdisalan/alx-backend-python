#!/usr/bin/env python3
"""Type-annotated function using TypeVar"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')  # Type variable for dictionary value type

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """Returns the value for the given key in the dictionary or a default value if the key does not exist"""
    if key in dct:
        return dct[key]
    else:
        return default
