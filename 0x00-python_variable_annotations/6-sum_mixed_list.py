#!/usr/bin/env python3
"""sum_mixed_list Module"""
from typing import List

def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """takes int and float, returns float"""
    return float(sum(mxd_lst))
