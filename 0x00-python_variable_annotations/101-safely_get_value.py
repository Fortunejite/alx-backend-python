#!/usr/bin/env python3
"""Basic annotations - safe first element of a sequence"""

from typing import Any, Union, TypeVar, Dict

def safely_get_value(dct: Dict, key: Any, default: Union[TypeVar('T'), None]) -> Union[Any, TypeVar('T')]:
    """Given parameters and the return values, add type annotations to the
    function"""
    if key in dct:
        return dct[key]
    else:
        return default
    