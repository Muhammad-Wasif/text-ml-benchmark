# Remote Text Data Access Client & REST API Guide

A production-grade, Kaggle-style remote data access system for the **[`Muhammad-Wasif/text-ml-benchmark`](https://github.com/Muhammad-Wasif/text-ml-benchmark)** dataset repository. Allows Python applications, machine learning engineers, and external services to discover, preview, load, stream, and download individual text datasets across 50 domains and 200 subtopics **without cloning the repository or downloading all data collections**.

---

## 1. System Architecture

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CLIENT APPLICATIONS                              │
│   (Python ML Scripts / Jupyter Notebooks / CLI Tools / Web Applications)   │
└──────────────────────┬───────────────────────────────┬──────────────────────┘
                       │                               │
        [Method A / B: Python Client]       [Method C: REST API]
                       │                               │
                       ▼                               ▼
       ┌───────────────────────────────┐   ┌───────────────────────────────┐
       │      github_data_client       │   │            api.py             │
       │     (GitHubDataClient)        │   │    (FastAPI REST Service)     │
       └───────────────┬───────────────┘   └───────────────┬───────────────┘
                       │                               │
                       ▼                               ▼
   ┌───────────────────────────────────────────────────────────────────────┐
   │                           GITHUB PLATFORM                             │
   │  - Raw URLs (raw.githubusercontent.com) [HTTP Range Previews]         │
   │  - GitHub REST API (api.github.com)     [Contents & Git Trees]        │
   │  - Public Access (Tokenless) OR Private Access (Bearer Token)         │
   └───────────────────────────────────────────────────────────────────────┘
```

The system provides three complementary access channels:
1. **Method A — Direct GitHub URL Access**: Tokenless, public raw content access with automatic conversion of GitHub file-page URLs (`/blob/...`) into raw stream requests.
2. **Method B — GitHub API Authentication**: Secure token authorization via environment variables (`GITHUB_TOKEN`) for private repositories and higher API rate limits.
3. **Method C — Custom FastAPI REST API**: A dedicated microservice exposing standard `/api/v1/...` endpoints for web frontends, microservices, and non-Python environments.

---

## 2. Installation & Quickstart

### Prerequisites
Python 3.9+ with standard scientific libraries:
```bash
pip install -r requirements.txt
```

### Optional Environment Setup (`.env`)
Copy `.env.example` to `.env` to configure optional authentication or server ports:
```bash
cp .env.example .env
```
Contents of `.env`:
```env
# Optional: Fine-grained or classic read-only GitHub token (Contents: Read)
GITHUB_TOKEN=your_token_here

# Target repository details
GITHUB_OWNER=Muhammad-Wasif
GITHUB_REPO=text-ml-benchmark
GITHUB_REF=main

# Custom API Server Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_KEY=
```

> [!IMPORTANT]
> `.env` is included in `.gitignore` by default. Never commit real tokens or credentials to source control. The client and API redact all tokens from error messages and logs.

---

## 3. Python Client (`GitHubDataClient`)

The client provides an interface similar to the Kaggle or Hugging Face dataset APIs, tailored for GitHub-hosted corpora.

### Basic Initialization
```python
from github_data_client import GitHubDataClient

# Public repository (zero tokens required)
client = GitHubDataClient(
    repository_url="https://github.com/Muhammad-Wasif/text-ml-benchmark",
    ref="main"
)
```

For private repositories, simply pass your token or set `GITHUB_TOKEN` in your environment:
```python
client = GitHubDataClient(
    repository_url="https://github.com/Muhammad-Wasif/text-ml-benchmark",
    token="ghp_your_read_only_token"
)
```

For reproducible research and model evaluation, bind the client to an **immutable commit SHA**:
```python
client = GitHubDataClient(ref="a23b02e70e9a7e80a0680eb80084ba55e97d21c3")
```

---

### Discovering Domains, Subtopics, and Files

#### List All 50 Real-World Domains
```python
domains = client.list_domains()
for d in domains[:5]:
    print(f"[{d['domain_id']}] {d['domain_name']} ({d['files_count']} files, {d['total_size_mb']} MB)")
```

#### List Subtopics in a Domain
```python
subtopics = client.list_subtopics(domain="23_pakistani_dramas")
for s in subtopics:
    print(f"Subtopic: {s['subtopic_name']} ({s['files_count']} files)")
```

#### Search the Data Catalog
```python
results = client.search("cricket batting", limit=5)
for item in results:
    print(f"Match: {item['title']} -> {item['path']}")
```

#### List Files by Filter
```python
# Filter by format and domain
files = client.list_files(domain="01_education_and_studying", format="json", limit=10)
for f in files:
    print(f"{f['file_id']} ({f['size_mb']} MB): {f['title']}")
```

---

### Memory-Efficient Previews

To inspect data without downloading large multi-megabyte files, use `client.preview()`:
- **HTTP Range Requests**: Only the first 64 KB are requested over the network.
- **Supported Formats**: CSV, TSV, JSON, JSONL, TXT, XML, Markdown.

```python
# Preview a large CSV without full download
preview = client.preview(
    "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv",
    limit=5
)

print("Columns:", preview["preview_data"]["columns"])
print("Sample Row:", preview["preview_data"]["rows"][0])
print("Is Truncated:", preview["is_truncated"])
```

```python
# Preview a 40 MB SQuAD v2.0 JSON dataset in under 0.2 seconds
preview = client.preview(
    "data/raw/01_education_and_studying/exam_preparation_and_revision/rajpurkar_squad_v2_train_corpus/train-v2.0.json",
    limit=2
)
print("Previewed SQuAD keys:", preview["preview_data"].keys())
```

---

### Loading Data Directly in Python

#### Tabular Data to Pandas DataFrame
```python
df = client.load_table(
    "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv"
)
print(df.head())
print("Shape:", df.shape)
```

#### Read Complete Text
```python
text = client.read_text(
    "data/raw/02_general_knowledge/historical_civilizations/project_gutenberg_edward_gibbon_decline_fall_vol3/gibbon_decline_and_fall_vol3.txt"
)
print(f"Loaded {len(text):,} characters.")
```

#### Memory-Constrained Streaming (Line-by-Line)
For multi-gigabyte or memory-constrained training jobs, stream lines without loading the whole file into RAM:
```python
file_path = "data/raw/25_books_and_literature/classic_literature_and_novels/project_gutenberg_jane_austen_emma/austen_emma.txt"
for line in client.stream_lines(file_path):
    if "Mr. Knightley" in line:
        print("Found line:", line.strip())
```

---

### Single-File Downloading with Checksum Verification

Download only the specific file needed, with automatic SHA-256 integrity verification:
```python
result = client.download(
    path_or_id="data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv",
    destination="./my_downloaded_data.csv",
    verify_checksum=True
)

print("Downloaded to:", result["destination"])
print("Bytes:", result["size_bytes"])
print("SHA-256 Validated:", result["checksum_verified"])
```

---

## 4. Command Line Interface (CLI)

The package includes a full CLI for terminal users:

```bash
# 1. List all 50 domains
python github_data_client.py domains

# 2. List subtopics in a domain
python github_data_client.py subtopics --domain "01_education_and_studying"

# 3. Filter files
python github_data_client.py files --domain "23_pakistani_dramas" --format json

# 4. Keyword search
python github_data_client.py search "neural networks"

# 5. Preview a file
python github_data_client.py preview "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv" --limit 5

# 6. Read text excerpt to stdout
python github_data_client.py read "data/raw/25_books_and_literature/classic_literature_and_novels/project_gutenberg_jane_austen_emma/austen_emma.txt" --head 300

# 7. Download a single file
python github_data_client.py download "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv" --out ./dataset.csv

# 8. Start the local FastAPI server
python github_data_client.py serve --port 8000
```

---

## 5. Custom Remote Data REST API (`api.py`)

A production FastAPI service that provides external microservices, mobile apps, or web dashboards with clean REST endpoints.

### Starting the Server
```bash
# Direct uvicorn execution
uvicorn api:app --host 0.0.0.0 --port 8000 --workers 4

# Or via client CLI
python github_data_client.py serve --port 8000
```
Interactive API docs are available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

### Endpoint Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/health` | Service health, repository name, branch, total files |
| `GET` | `/api/v1/domains` | List all 50 domains and aggregate metrics |
| `GET` | `/api/v1/domains/{domain}/subtopics` | Subtopics and file counts for a domain |
| `GET` | `/api/v1/files` | Query, filter, and search files (pagination supported) |
| `GET` | `/api/v1/files/{file_id}` | Complete verified metadata for a single file |
| `GET` | `/api/v1/files/{file_id}/preview` | Bounded memory-efficient preview (limit=20) |
| `GET` | `/api/v1/files/{file_id}/content` | Raw file text with appropriate `Content-Type` header |
| `GET` | `/api/v1/files/{file_id}/download` | Attachment download stream (`Content-Disposition`) |
| `GET` | `/api/v1/files/{file_id}/url` | Verified raw, web, and API URLs |

---

### REST API Examples (`curl`)

#### 1. Health Check
```bash
curl -X GET "http://localhost:8000/api/v1/health"
```
Response:
```json
{
  "status": "healthy",
  "repository": "Muhammad-Wasif/text-ml-benchmark",
  "owner": "Muhammad-Wasif",
  "ref": "main",
  "total_datasets": 536,
  "uptime_seconds": 12.45,
  "timestamp": 1793288595.82
}
```

#### 2. Search & Filter Files
```bash
curl -X GET "http://localhost:8000/api/v1/files?domain=cricket&format=json&limit=2"
```

#### 3. Preview File
```bash
curl -X GET "http://localhost:8000/api/v1/files/ds_01_education_and_studying_01_01_wikimedia_foundation/preview?limit=5"
```

#### 4. Stream Download File
```bash
curl -O -J -L "http://localhost:8000/api/v1/files/ds_01_education_and_studying_01_01_wikimedia_foundation/download"
```

---

## 6. Security & Performance Architecture

1. **Path Traversal Protection**: Every input path is sanitized against null bytes, `..` directory escapes, and root drive references. Invalid paths raise HTTP 400.
2. **SSRF Prevention**: All outbound HTTP requests are restricted to `github.com` and `raw.githubusercontent.com`.
3. **No Credential Leaking**: Personal access tokens are never logged, stored in error strings, or returned in API response bodies.
4. **Memory Safety**: Previews execute bounded HTTP Range byte fetches, preventing Out-Of-Memory (OOM) errors even on large datasets.
5. **Rate-Limit Intelligence**: If GitHub API rate limits are approached, the client raises `GitHubRateLimitError` indicating the exact UTC reset timestamp.

---

## 7. Troubleshooting

| Symptom | Cause | Solution |
|---|---|---|
| `GitHubNotFoundError (HTTP 404)` | File ID or path not found in catalog or repo | Check `client.list_files()` or verify spelling. |
| `GitHubRateLimitError (HTTP 403)` | GitHub unauthenticated IP rate limit reached | Provide a read-only token via `GITHUB_TOKEN=...`. |
| `SecurityError (HTTP 400)` | Path contains `..` or absolute drive letter | Pass repository-relative paths only (`data/raw/...`). |
| `GitHubAuthenticationError (HTTP 401)` | Token is expired or lacks read permissions | Generate a new token with **Contents: Read** permissions. |
