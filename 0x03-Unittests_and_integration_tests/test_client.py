#!/usr/bin/env python3
'''
Module to test functions in utils.py
'''
import unittest
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock
from unittest.mock import patch
from requests.exceptions import Timeout


class TestGithubOrgClient(unittest.TestCase):
    '''Test class for org method of TestGithubOrgClient'''
    @parameterized.expand([
        ('google', {"pay_load": True}),
        ('abc', {"pay_load": False}),
    ])
    @patch('client.get_json')
    def test_org(self, input, test_payload, moc_getjson):
        '''function to test org method'''
        moc_getjson.get_json.return_value = test_payload
        obj = GithubOrgClient(input)
        obj.org()
        moc_getjson.assert_called_once_with(
            'https://api.github.com/orgs/{inp}'.format(inp=input))
