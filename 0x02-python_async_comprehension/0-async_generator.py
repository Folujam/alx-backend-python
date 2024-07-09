#!/usr/bin/env python3
"""Async Generator Module"""
import asyncio
import random


async def async_generator():
    """loops 10 times, asynchronously waits 1sec, yeilds randnum"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
