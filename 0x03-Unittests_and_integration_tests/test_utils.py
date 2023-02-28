#!/usr/bin/env python3
"""Tests for utils.py"""

import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised for certain inputs"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        expected_msg = f'KeyError: "{path[-1]}"'
        self.assertEqual(str(error.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that utils.get_json returns the expected result"""
        with patch('requests.get') as mock_get:
            mock_get.return_value = unittest.mock.Mock()
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self):
        """Test that memoize decorator works as expected"""
        with unittest.mock.patch('utils.TestClass.a_method') as mock_a_method:
            mock_a_method.return_value = 42
            test_class = TestClass()
            result_1 = test_class.a_property
            result_2 = test_class.a_property
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
