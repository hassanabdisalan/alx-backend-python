#!/usr/bin/env python3
"""Test client module
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method
        """
        test_payload = {"payload": True}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url property
        """
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock,
            return_value={"repos_url": "http://test.url"}
        ) as mock_org:
            client = GithubOrgClient("test")
            self.assertEqual(
                client._public_repos_url,
                "http://test.url"
            )
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method
        """
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
            return_value="http://test.url"
        ) as mock_public_repos_url:
            client = GithubOrgClient("test")
            self.assertEqual(
                client.public_repos(),
                ["repo1", "repo2"]
            )
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class
    """
    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function"""
            if url.endswith("/orgs/google"):
                return Mock(json=lambda: cls.org_payload)
            elif url.endswith("/repos/google/repos"):
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: {})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method in integration"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
