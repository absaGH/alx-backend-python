#!/usr/bin/env ptyhon
'''
Module to test functions in utils.py
'''
from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    '''Test class for AccessNestedMap function'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            input1: Mapping,
            input2: Sequence,
            out: Any):
        '''tests AccessNestedMap function'''
        self.assertEqual(access_nested_map(input1, input2), out)
