#!/usr/bin/env python3
""" Test client
"""
from client import GithubOrgClient


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
        test_responnse = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()
