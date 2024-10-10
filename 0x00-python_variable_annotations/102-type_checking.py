#!/usr/bin/env python3
"""
Defines a function that zooms into a tuple by repeating its
elements based on a factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Repeats elements in a tuple based on the provided factor and returns a list
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)