#!/usr/bin/env python3
"""test_utils Module"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """test methods in utily.access_nested_map
    -access_nested_map(nested_map: Mapping, path: Sequence) -> Any
    -decorates the method
    """
    @parameterized.expand([
        ("nested_map", "path", 1),
        ("nested_map", "path", {"b": 2}),
        ("nested_map", "path", 2)
    ])
    def test_access_nested_map(self, nested_map, path, needed_result):
        """uses assertEqual to ensure result"""
        self.assertEquals(access_nested_map(nested_map, path), needed_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, needed_result):
        """uses assertRaises to raisee keyerror if 
         only above imputs"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEquals("KeyError {}".format(needed_result), repr(err.exception))
