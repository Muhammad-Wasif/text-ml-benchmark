"""
tests/test_client_catalog.py - Tests for catalog discovery, domain/subtopic listing, and search.
"""

import pytest
from github_data_client import GitHubDataClient, GitHubNotFoundError

@pytest.fixture
def client():
    return GitHubDataClient()

def test_list_domains_returns_all_50(client):
    domains = client.list_domains()
    assert len(domains) == 50
    domain_ids = [d["domain_id"] for d in domains]
    assert "01_education_and_studying" in domain_ids
    assert "23_pakistani_dramas" in domain_ids
    assert "50_non_political_news_and_current_events" in domain_ids

def test_list_subtopics_by_domain(client):
    subtopics = client.list_subtopics("01_education_and_studying")
    assert len(subtopics) >= 4
    subtopic_names = [s["subtopic_name"].lower() for s in subtopics]
    assert any("study techniques" in name for name in subtopic_names)

def test_list_files_with_filters(client):
    csv_files = client.list_files(format="csv")
    assert len(csv_files) > 0
    for f in csv_files:
        assert f["format"].lower() == "csv"

    edu_files = client.list_files(domain="01_education_and_studying")
    assert len(edu_files) > 0
    for f in edu_files:
        assert f["domain_id"] == "01_education_and_studying"

def test_search_keywords(client):
    results = client.search("cricket", limit=5)
    assert len(results) > 0
    assert any("cricket" in r["title"].lower() or "cricket" in r["path"].lower() for r in results)

def test_get_file_info_valid(client):
    files = client.list_files(limit=1)
    assert len(files) == 1
    sample = files[0]
    info = client.get_file_info(sample["file_id"])
    assert info["file_id"] == sample["file_id"]
    assert info["path"] == sample["path"]
    assert info["raw_url"].startswith("https://raw.githubusercontent.com")

def test_get_file_info_missing_raises_404(client):
    with pytest.raises(GitHubNotFoundError):
        client.get_file_info("non_existent_file_id_xyz")
