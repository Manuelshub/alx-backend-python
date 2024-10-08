#!/usr/bin/env python3
""" Test client
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Test github org client
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, org, mock_org):
        """ Test org
        """
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()
