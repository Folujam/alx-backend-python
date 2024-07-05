#!/usr/bin/env python3
"""typeAnnotation Module"""
from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
    """safely get value to key"""
    if key in dct:
        return dct[key]
    else:
        return default
