# Text-Based Machine Learning Benchmark Repository (50 Domains, 200 Subtopics)

An autonomous, curated, source-attributed text dataset repository designed for machine learning research, pre-training, fine-tuning, retrieval-augmented generation (RAG), and evaluation.

## 🚀 Quick Connect: Use This Data in Any App in Under 3 Lines of Code

We provide zero-dependency client connectors in Python and JavaScript so any external application or machine learning pipeline can connect immediately:

### Python Connector (`connect.py`)
```python
from connect import DatasetClient

client = DatasetClient()
for record in client.stream_records(domain='23_pakistani_dramas'):
    print(record['text'][:200])
```

### JavaScript / Node.js Connector (`connect.js`)
```javascript
const { DatasetClient } = require('./connect.js');

const client = new DatasetClient();
client.streamRecords({ domain: '01_education_and_studying' }, (rec) => {
  console.log(rec.text.slice(0, 200));
});
```

### Instant REST API Server
```bash
python connect.py --serve --port 8000
# External applications can query: http://localhost:8000/api/records?domain=23_pakistani_dramas
```

## 1. Repository Architecture & Layout

```text
text-ml-benchmark/ (RAW DATA/)
│
├── connect.py                # Zero-dependency Python Connector & REST API Server
├── connect.js                # Zero-dependency Node.js / JavaScript Connector
├── app_example.py            # Complete runnable 3-line application demonstration
├── data/
│   ├── raw/                  # Layer 1: Untouched, original raw downloads (550+ MB)
│   │   ├── 01_education_and_studying/
│   │   │   ├── study_techniques_and_learning_strategies/
│   │   │   │   └── wikimedia_foundation_.../
│   │   │   │       ├── study_skills_and_strategies.json
│   │   │   │       └── README.md
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

## 2. Key Inventory Metrics

- **Domains Covered:** 50 distinct real-world domains
- **Subtopics Covered:** 200 individual subtopics (4 per domain)
- **Total Preserved Datasets:** 536 (including supplementary multi-platform sources)
- **Subtopic Coverage Rate:** 100.0% (200 / 200 subtopics downloaded and verified)
- **Total Storage Volume:** 577,712,277 bytes (550.95 MB / 0.54 GB)
- **Source Diversity:** 6 verified open platforms (Hugging Face, GitHub, Zenodo, OpenML, Project Gutenberg, Wikimedia Foundation)

## 3. Cryptographic Verification

To verify repository integrity against unauthorized tampering or corruption, compare the files against `metadata/checksums.sha256`:
```powershell
Get-FileHash -Algorithm SHA256 (Get-ChildItem -Recurse data/raw/*.*) | Select-Object Hash, Path
```
