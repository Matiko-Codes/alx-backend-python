#!/usr/bin/env python3
"""
This module contains unit tests for the utils module
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """
        Test that access_nested_map raises a KeyError when an invalid key is provided
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_request):
        """
        Test get_json function
        """
        mock_request.return_value = Mock()
        mock_request.return_value.json.return_value = payload

        result = get_json(url)
        self.assertEqual(result, payload)
        mock_request.assert_called_once_with(url)

class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        with unittest.mock.patch('utils.TestClass.a_method') as mock_a_method:
            mock_a_method.return_value = 42
            test_class = TestClass()
            result_1 = test_class.a_property
            result_2 = test_class.a_property
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
            mock_a_method.assert_called_once()
