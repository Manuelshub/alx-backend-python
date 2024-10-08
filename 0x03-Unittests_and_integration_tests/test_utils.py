#!/usr/bin/env python3
""" Test utils
"""
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function."""
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test memoize
    """

    def test_memoize(self):
        """ Test memoize
        """
        class TestClass:
            """ Test class
            """

            def a_method(self):
                """ Test method
                """
                return 42

            @memoize
            def a_property(self):
                """ Test property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock.assert_called_once()
