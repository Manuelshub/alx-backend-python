#!/usr/bin/env python3
""" Test utils
"""
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access nested map exception
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test get json
    """

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """ Test get json
        """
        test_cases = [
            {
                "test_url": "http://example.com",
                "test_payload": {"payload": True}
            },
            {
                "test_url": "http://holberton.io",
                "test_payload": {"payload": False}
            },
        ]

        for case in test_cases:
            test_url = case["test_url"]
            test_payload = case["test_payload"]

            mock_response = Mock()
            mock_response.json.return_value = test_payload

            mock_get.return_value = mock_response

            reult = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(reult, test_payload)

            mock_get.reset_mock()
