"""
tests/test_client_security_and_auth.py - Tests for token handling, authentication errors, and security barriers.
"""

import pytest
from unittest.mock import patch, MagicMock
from github_data_client import (
    GitHubDataClient,
    GitHubAuthenticationError,
    GitHubRateLimitError,
    SecurityError
)

def test_token_header_injected_securely():
    fake_token = "ghp_FAKE_TEST_CREDENTIAL_TOKEN_12345"
    client = GitHubDataClient(token=fake_token)
    assert client._session.headers.get("Authorization") == f"Bearer {fake_token}"
    # Verify client representation does not leak token in repr/str
    assert fake_token not in repr(client)

def test_authentication_failure_raises_clean_error():
    client = GitHubDataClient(token="ghp_invalid_token_xyz")
    mock_resp = MagicMock()
    mock_resp.status_code = 401
    mock_resp.text = "Bad credentials"

    with patch.object(client._session, "request", return_value=mock_resp):
        with pytest.raises(GitHubAuthenticationError) as exc_info:
            client._request("GET", "https://api.github.com/repos/owner/repo/contents")
        # Ensure the actual secret token is NOT leaked in the error message
        assert "ghp_invalid_token_xyz" not in str(exc_info.value)
        assert "access denied" in str(exc_info.value).lower()

def test_rate_limit_exceeded_raises_clean_error():
    client = GitHubDataClient()
    mock_resp = MagicMock()
    mock_resp.status_code = 403
    mock_resp.text = "API rate limit exceeded for user"
    mock_resp.headers = {"X-RateLimit-Reset": "1793290000"}

    with patch.object(client._session, "request", return_value=mock_resp):
        with pytest.raises(GitHubRateLimitError) as exc_info:
            client._request("GET", "https://api.github.com/repos/owner/repo/contents")
        assert "rate limit exceeded" in str(exc_info.value).lower()

def test_path_traversal_blocked_on_read():
    client = GitHubDataClient()
    with pytest.raises(SecurityError):
        client.read_text("../../etc/passwd")

def test_path_traversal_blocked_on_preview():
    client = GitHubDataClient()
    with pytest.raises(SecurityError):
        client.preview("../../../secret.json")
