#!/usr/bin/env python3
'''
Module to test functions in utils.py
'''
import unittest
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, PropertyMock
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

    def test_public_repos_url(self):
        '''function to test _public_repos_url() method'''
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as moc_obj:
            payload = {'repos_url': 'https://api.github.com/orgs/google/repos'}
            moc_obj.return_value = payload
            obj = GithubOrgClient('google')
            test_return = obj._public_repos_url
            self.assertEqual(test_return,
                             moc_obj.return_value.get('repos_url'))
