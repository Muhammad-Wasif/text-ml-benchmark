"""
tests/test_api_endpoints.py - Automated tests for the FastAPI REST API service.
"""

import pytest
from starlette.testclient import TestClient
from api import app

@pytest.fixture
def client():
    return TestClient(app)

def test_api_health(client):
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "healthy"
    assert "repository" in data
    assert data["total_datasets"] == 536

def test_api_domains_listing(client):
    r = client.get("/api/v1/domains")
    assert r.status_code == 200
    domains = r.json()
    assert len(domains) == 50
    assert domains[0]["domain_id"] == "01_education_and_studying"

def test_api_domain_subtopics(client):
    r = client.get("/api/v1/domains/01_education_and_studying/subtopics")
    assert r.status_code == 200
    subtopics = r.json()
    assert len(subtopics) >= 4

def test_api_domain_not_found(client):
    r = client.get("/api/v1/domains/invalid_domain_12345/subtopics")
    assert r.status_code == 404

def test_api_files_pagination_and_filter(client):
    r = client.get("/api/v1/files?domain=01_education_and_studying&format=json&limit=5")
    assert r.status_code == 200
    data = r.json()
    assert data["limit"] == 5
    assert len(data["files"]) <= 5
    for f in data["files"]:
        assert f["format"].lower() == "json"

def test_api_file_metadata_and_404(client):
    # Valid file
    files_resp = client.get("/api/v1/files?limit=1")
    file_id = files_resp.json()["files"][0]["file_id"]

    r = client.get(f"/api/v1/files/{file_id}")
    assert r.status_code == 200
    assert r.json()["file_id"] == file_id

    # Invalid file
    r_bad = client.get("/api/v1/files/non_existent_file_9999")
    assert r_bad.status_code == 404

def test_api_file_preview(client):
    files_resp = client.get("/api/v1/files?limit=1")
    file_id = files_resp.json()["files"][0]["file_id"]

    r = client.get(f"/api/v1/files/{file_id}/preview?limit=10")
    assert r.status_code == 200
    data = r.json()
    assert data["file_id"] == file_id
    assert "preview_data" in data

def test_api_file_content(client):
    files_resp = client.get("/api/v1/files?format=json&limit=1")
    file_id = files_resp.json()["files"][0]["file_id"]

    r = client.get(f"/api/v1/files/{file_id}/content")
    assert r.status_code == 200
    assert "application/json" in r.headers["content-type"]
    assert len(r.text) > 0

def test_api_file_download_stream(client):
    files_resp = client.get("/api/v1/files?limit=1")
    file_id = files_resp.json()["files"][0]["file_id"]

    r = client.get(f"/api/v1/files/{file_id}/download")
    assert r.status_code == 200
    assert "attachment" in r.headers.get("content-disposition", "")
    assert len(r.content) > 0

def test_api_file_urls(client):
    files_resp = client.get("/api/v1/files?limit=1")
    file_id = files_resp.json()["files"][0]["file_id"]

    r = client.get(f"/api/v1/files/{file_id}/url")
    assert r.status_code == 200
    data = r.json()
    assert data["raw_url"].startswith("https://raw.githubusercontent.com")
    assert data["blob_url"].startswith("https://github.com")

def test_api_path_traversal_blocked(client):
    r = client.get("/api/v1/files/..%2F..%2Fetc%2Fpasswd/content")
    assert r.status_code in [400, 404]
