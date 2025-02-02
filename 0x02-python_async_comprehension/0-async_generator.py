#!/usr/bin/env python3
"""Async Generator Module"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """loops 10 times, asynchronously waits 1sec, yeilds randnum"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
