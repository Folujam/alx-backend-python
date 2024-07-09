#!/usr/bin/env python3
"""Async Comprehension Module"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """from async_generator creates 10 randnums"""
    return [randnum async for randnum in async_generator()]
