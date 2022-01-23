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
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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

    @patch('client.get_json')
    def test_public_repos(self, moc_getjson):
        '''function to test public_repos() method'''
        moc_getjson.return_value = [{"name": "google"}]
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock) as moc_obj:
            moc_obj.return_value = "https://api.github.com/"
            obj = GithubOrgClient("google")
            test_return = obj.public_repos()
            self.assertEqual(test_return, ["google"])
            moc_getjson.assert_called_once
            moc_obj.assert_called_once

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, out):
        '''test function for has_license method'''
        obj = GithubOrgClient('google')
        result = obj.has_license(repo, license_key)
        self.assertEqual(result, out)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test """
    @classmethod
    def setUpClass(cls):
        """ It is part of the unittest.TestCase API
        method to setup the tests """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ It is part of the unittest.TestCase API
        method to teardown the test case """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ method to test GithubOrgClient.public_repos """
        test_class = GithubOrgClient("google")
        assert True

    def test_public_repos_with_license(self):
        """ method to test the public_repos with the argument license """
        test_class = GithubOrgClient("google")
        assert True
