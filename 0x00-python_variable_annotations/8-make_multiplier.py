#!/usr/bin/env python3
"""Basic annotations - make multiplier"""


def make_multiplier(multiplier: float):
    """Returns a function that multiplies a float by multiplier."""
    def multiply_by_multiplier(n: float) -> float:
        """Returns the product of multiplier and n."""
        return (n * multiplier)
    return multiply_by_multiplier
