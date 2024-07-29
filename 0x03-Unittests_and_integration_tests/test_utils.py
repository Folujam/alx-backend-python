#!/usr/bin/env python3
"""test_utils Module"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Tuple, Dict


class TestAccessNestedMap(unittest.TestCase):
    """test methods in utily.access_nested_map
    -access_nested_map(nested_map: Mapping, path: Sequence) -> Any
    -decorates the method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple,
                               needed_result: int):
        """uses assertEqual to ensure result"""
        self.assertEqual(access_nested_map(nested_map, path), needed_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple,
                                         needed_result: int):
        """uses assertRaises to raisee keyerror if
         only above imputs"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual("KeyError {}".format(needed_result),
                          repr(err.exception))
