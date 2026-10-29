# Text-Based Machine Learning Benchmark Repository (50 Domains, 200 Subtopics)

An autonomous, curated, source-attributed text dataset repository designed for machine learning research, pre-training, fine-tuning, retrieval-augmented generation (RAG), and evaluation.

Contains **550.95 MB** of authentic raw text data across **50 real-world domains** and **200 individual subtopics**, complete with zero-dependency connectors, a full remote Python client, and a FastAPI REST service.

---

## 🚀 Remote Data Access: Kaggle-Style Access from Anywhere

You can discover, preview, load, stream, and download individual datasets remotely from GitHub **without cloning the entire repository or downloading all data collections**:

### 1. Python Client ([`github_data_client.py`](file:///C:/Users/Admin/Desktop/RAW%20DATA/github_data_client.py))
```python
from github_data_client import GitHubDataClient

# Initialize without tokens for public access
client = GitHubDataClient(repository_url="https://github.com/Muhammad-Wasif/text-ml-benchmark")

# 1. Discover domains
domains = client.list_domains()

# 2. Preview a large file in memory-efficient mode (HTTP Range request)
preview = client.preview(
    "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv",
    limit=5
)
print("Preview columns:", preview["preview_data"]["columns"])

# 3. Load directly into a pandas DataFrame
df = client.load_table(
    "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv"
)

# 4. Download ONLY this specific file with SHA-256 verification
client.download(
    "data/raw/01_education_and_studying/academic_performance_and_study_habits/github_student_study_habits_and_acade/student_study_habits_performance.csv",
    destination="./my_dataset.csv"
)
```

### 2. Command-Line Interface (CLI)
```bash
# List domains
python github_data_client.py domains

# Search across 50 domains
python github_data_client.py search "neural networks"

# Preview a file
python github_data_client.py preview "data/raw/01_education_and_studying/exam_preparation_and_revision/rajpurkar_squad_v2_train_corpus/train-v2.0.json" --limit 5

# Download a single file
python github_data_client.py download "data/raw/25_books_and_literature/classic_literature_and_novels/project_gutenberg_jane_austen_emma/austen_emma.txt"
```

### 3. Production REST API ([`api.py`](file:///C:/Users/Admin/Desktop/RAW%20DATA/api.py))
```bash
# Start the FastAPI server
uvicorn api:app --host 0.0.0.0 --port 8000
# Or via CLI
python github_data_client.py serve --port 8000

# Access interactive documentation:
# Swagger UI: http://localhost:8000/docs
# ReDoc:      http://localhost:8000/redoc
```

> [!TIP]
> For complete documentation on all methods, authentication, API routes, and deployment options, see **[`CLIENT_GUIDE.md`](file:///C:/Users/Admin/Desktop/RAW%20DATA/CLIENT_GUIDE.md)**.

---

## ⚡ Zero-Dependency 3-Line Connectors

For quick local embedding in lightweight scripts:

### Python Connector ([`connect.py`](file:///C:/Users/Admin/Desktop/RAW%20DATA/connect.py))
```python
from connect import DatasetClient

client = DatasetClient()
for record in client.get(domain="pakistani_dramas", limit=5):
    print(record["text"][:150])
```

### JavaScript / Node.js Connector ([`connect.js`](file:///C:/Users/Admin/Desktop/RAW%20DATA/connect.js))
```javascript
const { DatasetClient } = require('./connect.js');

const client = new DatasetClient();
console.log(client.get({ domain: "education", limit: 5 }));
```

---

## 1. Repository Architecture & Layout

```text
text-ml-benchmark/ (RAW DATA/)
│
├── github_data_client.py     # Universal Remote Python Client & CLI
├── api.py                    # FastAPI REST API Service (Endpoints: /api/v1/...)
├── CLIENT_GUIDE.md           # Comprehensive Client & REST API Technical Guide
├── requirements.txt          # Python dependencies (fastapi, uvicorn, pandas, pytest, etc.)
├── .env.example              # Environment variables template
├── connect.py                # Zero-dependency Python Connector
├── connect.js                # Zero-dependency Node.js / JavaScript Connector
├── app_example.py            # Complete runnable 3-line application demonstration
├── tests/                    # Automated Test Suite (39 unit & integration tests)
│   ├── test_url_parser.py
│   ├── test_client_catalog.py
│   ├── test_client_preview_and_load.py
│   ├── test_client_download.py
│   ├── test_client_security_and_auth.py
│   ├── test_api_endpoints.py
│   └── test_remote_live.py
│
├── data/
│   ├── raw/                  # Layer 1: Untouched, original raw downloads (550.95 MB)
│   │   ├── 01_education_and_studying/
│   │   │   ├── study_techniques_and_learning_strategies/
│   │   │   ├── exam_preparation_and_revision/
│   │   │   ├── student_time_management/
│   │   │   └── academic_performance_and_study_habits/
│   │   ├── 02_general_knowledge/
│   │   ├── ... (50 distinct domain directories)
│   │   └── 50_non_political_news_and_current_events/
│   │
│   └── training_exports/     # Layer 2: Standardized streaming JSONL
│       └── all_domains_benchmark.jsonl
│
├── metadata/
│   ├── dataset_registry.jsonl# Master machine-readable registry (JSON Lines)
│   ├── domain_coverage.csv   # Summary coverage across all 50 domains
│   ├── subtopic_coverage.csv # Granular coverage table across all 200 subtopics
│   ├── source_audit.csv      # Platform and licensing audit
│   ├── download_failures.csv # External platform limitation audit
│   └── checksums.sha256      # SHA-256 cryptographic verification file
│
├── reports/
│   ├── research_summary.md   # High-level curation overview
│   ├── data_quality_report.md# Text fields, formats, and structural audit
│   ├── licensing_report.md   # License compliance and terms of use
│   └── missing_subtopics.md  # Gap analysis and download limitation report
│
└── README.md                 # Master repository documentation
```

---

## 2. Key Inventory Metrics

- **Domains Covered:** 50 distinct real-world domains
- **Subtopics Covered:** 200 individual subtopics (4 per domain)
- **Total Preserved Datasets:** 536 (including supplementary multi-platform sources)
- **Subtopic Coverage Rate:** 100.0% (200 / 200 subtopics downloaded and verified)
- **Total Storage Volume:** 577,712,277 bytes (550.95 MB / 0.54 GB)
- **Source Diversity:** 6 verified open platforms (Hugging Face, GitHub, Zenodo, OpenML, Project Gutenberg, Wikimedia Foundation)
- **Automated Test Suite:** 100% test pass rate across 40 test cases (`pytest tests/`)

---

## 3. Running Automated Tests

Run the complete test suite to verify public access, URL parsing, previews, DataFrame loading, single-file downloads, and REST API endpoints:
```bash
pytest tests/ -v
```

---

## 4. Cryptographic Verification

To verify repository integrity against unauthorized tampering or corruption, compare the files against `metadata/checksums.sha256`:
```powershell
Get-FileHash -Algorithm SHA256 (Get-ChildItem -Recurse data/raw/*.*) | Select-Object Hash, Path
```
