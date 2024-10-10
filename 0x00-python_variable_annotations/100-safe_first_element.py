#!/usr/bin/env python3
"""
Defines a function that returns the first element of a sequence, if it exists.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
