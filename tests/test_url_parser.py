"""
tests/test_url_parser.py - Tests for GitHub URL parsing, normalization, and path security.
"""

import pytest
from github_data_client import parse_github_url, sanitize_path, SecurityError

def test_parse_standard_repo_url():
    res = parse_github_url("https://github.com/Muhammad-Wasif/text-ml-benchmark")
    assert res["owner"] == "Muhammad-Wasif"
    assert res["repo"] == "text-ml-benchmark"
    assert res["ref"] == "main"
    assert res["path"] is None
    assert res["is_raw"] is False

def test_parse_repo_url_with_git_suffix():
    res = parse_github_url("https://github.com/Muhammad-Wasif/text-ml-benchmark.git")
    assert res["owner"] == "Muhammad-Wasif"
    assert res["repo"] == "text-ml-benchmark"

def test_parse_blob_url():
    url = "https://github.com/Muhammad-Wasif/text-ml-benchmark/blob/main/data/raw/01_education_and_studying/file.txt"
    res = parse_github_url(url)
    assert res["owner"] == "Muhammad-Wasif"
    assert res["repo"] == "text-ml-benchmark"
    assert res["ref"] == "main"
    assert res["path"] == "data/raw/01_education_and_studying/file.txt"
    assert res["is_raw"] is False

def test_parse_raw_url():
    url = "https://raw.githubusercontent.com/Muhammad-Wasif/text-ml-benchmark/v1.0.0/data/raw/data.csv"
    res = parse_github_url(url)
    assert res["owner"] == "Muhammad-Wasif"
    assert res["repo"] == "text-ml-benchmark"
    assert res["ref"] == "v1.0.0"
    assert res["path"] == "data/raw/data.csv"
    assert res["is_raw"] is True

def test_parse_short_repo_slug():
    res = parse_github_url("Muhammad-Wasif/text-ml-benchmark")
    assert res["owner"] == "Muhammad-Wasif"
    assert res["repo"] == "text-ml-benchmark"
    assert res["ref"] == "main"

def test_parse_unauthorized_domain_rejected():
    with pytest.raises(SecurityError, match="Unsupported domain"):
        parse_github_url("https://malicious-site.com/repo/file.txt")

def test_sanitize_path_valid():
    assert sanitize_path("data/raw/domain/file.csv") == "data/raw/domain/file.csv"
    assert sanitize_path("data\\raw\\domain\\file.csv") == "data/raw/domain/file.csv"
    assert sanitize_path("./data/raw/file.txt") == "data/raw/file.txt"

def test_sanitize_path_traversal_rejected():
    with pytest.raises(SecurityError, match="Path traversal"):
        sanitize_path("../secret/password.txt")

    with pytest.raises(SecurityError, match="Path traversal"):
        sanitize_path("data/raw/../../etc/passwd")

def test_sanitize_path_absolute_rejected():
    with pytest.raises(SecurityError, match="Absolute paths are forbidden"):
        sanitize_path("/etc/shadow")

    with pytest.raises(SecurityError, match="Absolute paths are forbidden"):
        sanitize_path("C:/Windows/System32")

def test_sanitize_path_null_byte_rejected():
    with pytest.raises(SecurityError, match="Null bytes are forbidden"):
        sanitize_path("data/raw/file\0.txt")
