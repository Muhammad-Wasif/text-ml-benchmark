"""
tests/test_client_download.py - Tests for single-file selective downloading and checksum verification.
"""

import os
import tempfile
import pytest
from github_data_client import GitHubDataClient

@pytest.fixture
def client():
    return GitHubDataClient()

def test_single_file_download_to_destination(client):
    csv_path = "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv"
    with tempfile.TemporaryDirectory() as tmpdir:
        dest_file = os.path.join(tmpdir, "my_custom_download.csv")
        res = client.download(csv_path, destination=dest_file, verify_checksum=True)

        assert res["status"] == "success"
        assert res["destination"] == os.path.abspath(dest_file)
        assert os.path.isfile(dest_file)
        assert os.path.getsize(dest_file) > 0
        assert res["checksum_verified"] is True
        assert len(res["sha256"]) == 64

        # Verify ONLY this single file was created in tmpdir
        files_in_tmp = os.listdir(tmpdir)
        assert files_in_tmp == ["my_custom_download.csv"]
