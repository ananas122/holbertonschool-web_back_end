#!/usr/bin/env python3
""" Unittests for client.py """

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test org method """
        mock_get_json.return_value = {"name": org_name}
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, {"name": org_name})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ Test _public_repos_url method """
        org_name = "google"
        repo_url = f"https://api.github.com/orgs/{org_name}"
        mock_org.return_value = {"repos_url": repo_url}
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client._public_repos_url, repo_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test public_repos method """
        mock_get_json.return_value = [
            {"name": "google"},
            {"name": "abc"}
        ]
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            github_org_client = GithubOrgClient("google")
            repos = github_org_client.public_repos()
            self.assertEqual(repos, ["google", "abc"])
            mock_get_json.assert_called_once()
            mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has_license method """
        github_org_client = GithubOrgClient("org_name")
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
     GithubOrgClient.public_repos method in an integration test.
     That means that we will only mock code that sends external requests.
    """

    @classmethod
    def setUpClass(cls):
        """
        set up
        """
        cls.get_patcher = patch('requests.get')
        cls.mc = cls.get_patcher.start()
        cls.mc.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """
        tear down
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        """
        testClass = GithubOrgClient(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )
        self.assertEqual(testClass.org, self.org_payload)
        self.assertEqual(testClass.repos_payload, self.repos_payload)

    def test_public_repos_with_license(self):
        """
        """
        testClass = GithubOrgClient(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )
        self.assertEqual(testClass.public_repos(license="apache-2.0"),
                         self.apache2_repos)
