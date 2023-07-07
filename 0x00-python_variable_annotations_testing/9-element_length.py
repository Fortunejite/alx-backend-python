#!/usr/bin/env python3
"""Basic annotations - to string"""


def element_length(lst: list[str]) -> list[tuple[str, int]]:
    return [(i, len(i)) for i in lst]
