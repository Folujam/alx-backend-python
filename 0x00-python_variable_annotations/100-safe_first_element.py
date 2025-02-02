#!/usr/bin/env python3
"""duck typed Module"""
from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """list takes any type,
        returns any or none"""
    if lst:
        return lst[0]
    else:
        return None
