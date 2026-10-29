"""
tests/test_client_preview_and_load.py - Tests for previewing, reading, and loading tabular data.
"""

import pytest
import pandas as pd
from github_data_client import GitHubDataClient

@pytest.fixture
def client():
    return GitHubDataClient()

def test_preview_csv_bounded_rows(client):
    csv_path = "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv"
    preview = client.preview(csv_path, limit=5)
    assert preview["format"] == "csv"
    assert preview["limit"] == 5
    pdata = preview["preview_data"]
    assert "columns" in pdata
    assert "rows" in pdata
    assert len(pdata["rows"]) == 5
    assert len(pdata["columns"]) > 0

def test_preview_json_bounded(client):
    json_path = "data/raw/01_education_and_studying/exam_preparation_and_revision/rajpurkar_squad_v2_train_corpus/train-v2.0.json"
    preview = client.preview(json_path, limit=3)
    assert preview["format"] == "json"
    assert preview["is_truncated"] is True
    assert preview["size_bytes"] > 40 * 1024 * 1024  # >40 MB
    assert preview["preview_data"] is not None

def test_preview_txt_bounded_lines(client):
    txt_path = "data/raw/02_general_knowledge/historical_civilizations/project_gutenberg_edward_gibbon_decline_fall_vol3/gibbon_decline_and_fall_vol3.txt"
    preview = client.preview(txt_path, limit=10)
    assert preview["format"] == "txt"
    lines = preview["preview_data"].splitlines()
    assert len(lines) <= 10

def test_load_table_returns_dataframe(client):
    csv_path = "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv"
    df = client.load_table(csv_path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert "Hours Studied" in df.columns

def test_read_text_content(client):
    txt_files = client.list_files(format="txt", limit=1)
    assert len(txt_files) > 0
    content = client.read_text(txt_files[0]["path"])
    assert isinstance(content, str)
    assert len(content) > 0

def test_stream_lines_generator(client):
    txt_files = client.list_files(format="txt", limit=1)
    generator = client.stream_lines(txt_files[0]["path"])
    first_lines = []
    for line in generator:
        first_lines.append(line)
        if len(first_lines) >= 5:
            break
    assert len(first_lines) == 5
