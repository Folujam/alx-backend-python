#!/usr/bin/env python3
"""sum_mixed_list Module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes int and float, returns float"""
    return float(sum(mxd_lst))
