#!/usr/bin/env python3
"""Module for task 7"""


from typing import Tuple, Union
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the first element of the tuple being the string
    and the second element being the square of the int or float."""
    return (k, v * v)
