#!/usr/bin/env python3
"""typeAnnotation Module"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safely get value to key"""
    if key in dct:
        return dct[key]
    else:
        return default
