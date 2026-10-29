"""
tests/test_remote_live.py - Tests live remote fetching with local_fallback=False.
"""

import pytest
from github_data_client import GitHubDataClient

def test_remote_live_fetch():
    # Force pure remote mode without touching local files
    client = GitHubDataClient(
        repository_url="https://github.com/Muhammad-Wasif/text-ml-benchmark",
        ref="main",
        local_fallback=False
    )
    # 1. Remote catalog load
    domains = client.list_domains()
    assert len(domains) == 50

    # 2. Remote file preview using HTTP Range request
    csv_path = "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv"
    preview = client.preview(csv_path, limit=3)
    assert preview["format"] == "csv"
    assert len(preview["preview_data"]["rows"]) == 3
    assert preview["preview_data"]["columns"] is not None

    # 3. Remote URL generation
    raw_url = client.get_url(csv_path, raw=True)
    assert raw_url.startswith("https://raw.githubusercontent.com/Muhammad-Wasif/text-ml-benchmark/main/")
