#!/usr/bin/env python3
"""
Defines a function to safely get a value from a dictionary using a key.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary given a key, or returns a default.
    """
    if key in dct:
        return dct[key]
    else:
        return default