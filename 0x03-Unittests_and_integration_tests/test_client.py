#!/usr/bin/env python3
"""
Unittests for client.GithubOrgClient class
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = org_name
        github_org = GithubOrgClient(org_name)
        self.assertEqual(github_org.org, org_name)
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
