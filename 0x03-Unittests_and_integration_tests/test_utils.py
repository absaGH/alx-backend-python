#!/usr/bin/env python3
'''
Module to test functions in utils.py
'''
from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    '''Test class for AccessNestedMap function'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, out):
        '''tests AccessNestedMap function'''
        self.assertEqual(access_nested_map(nested_map, path), out)
