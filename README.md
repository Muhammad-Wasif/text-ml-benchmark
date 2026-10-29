# 🌍 50-Domain Real-World Text ML Benchmark & Dataset Repository

[![License: CC-BY-SA 4.0](https://img.shields.io/badge/License-CC--BY--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domains](https://img.shields.io/badge/Domains-50%20Real--World-brightgreen.svg)]()
[![Subtopics](https://img.shields.io/badge/Subtopics-200%20Verified-blueviolet.svg)]()
[![Records](https://img.shields.io/badge/Training%20Records-1%2C322%20Standardized-orange.svg)]()
[![Status](https://img.shields.io/badge/Coverage-100%25%20Verified-success.svg)]()

An autonomous, comprehensive, text-based machine learning dataset repository spanning **50 distinct real-world domains** and **200 individual subtopics**. Strictly text-based, verified from authentic sources (Hugging Face, GitHub, Zenodo, OpenML, Project Gutenberg, Wikimedia Foundation), with zero synthetic or fabricated records.

---

## ⚡ 30-Second Quickstart: Connect to Any App

We built ready-to-use, zero-dependency connectors so you can plug this entire dataset into any **Python**, **JavaScript / Node.js**, or **Web / Mobile REST API** application in 3 lines of code.

### 🐍 Option 1: Python (3 Lines)

```python
from connect import DatasetClient
client = DatasetClient()

# 1. Fetch records for any domain (e.g. cricket, pakistani dramas, astronomy)
records = client.get(domain="cricket", limit=5)
print(records[0]["text"])

# 2. Search across all 50 domains (instant RAG context retrieval)
results = client.search(query="climate change temperature", limit=3)
```

---

### 🟨 Option 2: JavaScript / Node.js (3 Lines)

```javascript
const { DatasetClient } = require("./connect.js");
const client = new DatasetClient();

// 1. Fetch records by domain or subtopic
const records = client.get({ domain: "cricket", limit: 5 });
console.log(records[0].text);

// 2. Search across all 50 domains
const matches = client.search("machine learning concepts", 3);
```

---

### 🚀 Option 3: Instant Local REST API (for React, Next.js, Mobile, or cURL)

Start the built-in, zero-dependency local REST API server:

```bash
python connect.py --serve --port 8000
```

Now any frontend, backend, or mobile app can query it:

```bash
# Get summary stats
curl "http://localhost:8000/api/stats"

# Get all 50 domains
curl "http://localhost:8000/api/domains"

# Query data by domain
curl "http://localhost:8000/api/data?domain=pakistani_dramas&limit=5"

# Search text across all 200 subtopics
curl "http://localhost:8000/api/search?q=space+exploration&limit=3"
```

Interactive API documentation and web UI is available at [`http://localhost:8000/docs`](http://localhost:8000/docs) when the server is running.

---

### 🦜🔗 Option 4: Plug into LangChain / LlamaIndex / RAG

```python
from connect import DatasetClient
from langchain_core.documents import Document

client = DatasetClient()

# Convert any domain into LangChain Document objects
docs = [
    Document(
        page_content=item["text"],
        metadata={"domain": item["domain"], "subtopic": item["subtopic"], "source": item["source"]}
    )
    for item in client.get(domain="artificial intelligence")
]
# Now pass `docs` directly to your VectorStore (FAISS, Chroma, Pinecone)!
```

---

## 📁 Repository Structure

```text
RAW DATA/
│
├── connect.py                       # Zero-dependency Python client & REST API server
├── connect.js                       # Zero-dependency Node.js client
├── app_example.py                   # Ready-to-run 30-second app integration example
│
├── data/
│   ├── raw/                         # LAYER 1: Untouched original raw source artifacts
│   │   ├── 01_education_and_studying/
│   │   │   ├── study_techniques_and_learning_strategies/
│   │   │   ├── exam_preparation_and_revision/
│   │   │   ├── student_time_management/
│   │   │   └── academic_performance_and_study_habits/
│   │   ├── 02_general_knowledge/
│   │   ├── ... (50 distinct domain folders)
│   │   └── 50_non_political_news_and_current_events/
│   │
│   └── training_exports/            # LAYER 2: Unified JSONL exports for ML training
│       └── all_domains_benchmark.jsonl
│
├── metadata/
│   ├── dataset_registry.jsonl       # Master machine-readable JSONL registry (204 entries)
│   ├── domain_coverage.csv          # Domain-level summary across all 50 domains
│   ├── subtopic_coverage.csv        # Subtopic coverage across all 200 subtopics
│   ├── source_audit.csv             # Platform breakdown & license verification
│   ├── download_failures.csv        # Documented platform access limitations
│   └── checksums.sha256             # 207 SHA-256 cryptographic hashes
│
├── reports/
│   ├── research_summary.md          # Comprehensive executive summary & coverage matrix
│   ├── data_quality_report.md       # Format distribution, text fields, and quality audit
│   ├── licensing_report.md          # Provenance, legal compliance, and terms of use
│   └── missing_subtopics.md         # 0-gap resolution & download failure audit
│
├── catalog_definitions.py           # Formal Python taxonomy specification
├── pipeline_executor.py             # Master download & verification engine
├── add_supplementary_datasets.py    # Multi-platform supplementary curator
└── README.md                        # Master repository documentation
```

---

## 📊 Key Repository Statistics

| Dimension | Metric | Notes |
|---|---|---|
| **Domains** | **50** | 100% accounted for across science, humanities, tech, everyday life |
| **Subtopics** | **200** | 4 subtopics per domain, individually researched and verified |
| **Preserved Datasets** | **204** | Includes multi-source coverage (Zenodo ZIP, OpenML ARFF, etc.) |
| **Total Raw Volume** | **19.14 MB** | Pure text-based records (JSON, CSV, ARFF, Parquet, TXT, ZIP) |
| **Training Records** | **1,322** | Pre-processed, standardized JSONL records ready for tokenization |
| **Data Sources** | **6 Platforms** | Hugging Face, GitHub, Zenodo, OpenML, Project Gutenberg, Wikimedia |
| **Integrity** | **207 Checksums** | SHA-256 computed for all raw and extracted archive files |

---

## 🌐 The 50 Domains (200 Subtopics)

<details>
<summary><b>Click to expand the complete 50-Domain Inventory</b></summary>

### Category A — Education, knowledge, and science
1. **Education and studying:** Study techniques, Exam preparation, Student time management, Academic performance
2. **General knowledge:** World geography, Historical civilizations, Discoveries & inventions, Everyday world facts
3. **Mathematics:** Arithmetic & percentages, Algebra & equations, Geometry & measurements, Statistics & probability
4. **Physics and chemistry:** Motion & force, Electricity & magnetism, Chemical reactions, Materials properties
5. **Space and the universe:** Planets & solar system, Stars & galaxies, Black holes, Space exploration & astronomy

### Category B — Nature, environment, and agriculture
6. **Nature and ecosystems:** Forests, Mountains & valleys, Rivers & lakes, Deserts & grasslands
7. **Trees and plants:** Tree species & uses, Plant reproduction, Gardening & plant care, Medicinal plants
8. **Animals and wildlife:** Mammals & behavior, Birds & migration, Marine animals, Wildlife conservation
9. **Agriculture and farming:** Crop cultivation, Soil fertility, Irrigation & water management, Harvesting & storage
10. **Weather and climate:** Rainfall & seasons, Temperature & humidity, Storms & severe weather, Climate patterns

### Category C — Household and everyday life
11. **Household management:** Cleaning & organization, Laundry care, Home maintenance, Daily routines
12. **Cooking and food:** Recipes & cooking methods, Ingredients & substitutions, Food preservation, Meal planning
13. **Personal finance:** Monthly budgeting, Saving money, Managing expenses, Cost & value comparison
14. **Shopping and consumer products:** Product specs, Price & quality comparisons, Customer reviews, Warranties & returns
15. **Daily routines and productivity:** Morning & evening routines, Task prioritization, Habit formation, Distraction management

### Category D — Health, fitness, and personal development
16. **General health education:** Common illnesses, Preventive health, Hygiene & infection control, Medical terminology
17. **Mental health and wellbeing:** Stress management, Emotional awareness, Relaxation & mindfulness, Coping strategies
18. **Fitness and exercise:** Cardiovascular exercise, Strength training, Flexibility & mobility, Recovery periodization
19. **Gym and bodybuilding:** Workout splits (PPL), Muscle exercise selection, Progressive overload, Sleep & rest
20. **Nutrition and diet:** Macronutrients & micronutrients, Balanced meal plans, Hydration, Food labels

### Category E — Entertainment and media
21. **Movies and cinema:** Film genres, Movie reviews, Filmmaking & production, Box office performance
22. **Television series:** Episode summaries, Character development, Season comparisons, Story structure
23. **Pakistani dramas:** Drama summaries & themes, Character relationships, Acting & direction, Audience ratings
24. **Online streaming platforms:** Subscription plans, Content recommendation, Viewing habits, Platform usability
25. **Books and literature:** Fiction genres, Book summaries, Authorial styles, Themes & symbolism

### Category F — Sports, hobbies, and recreation
26. **Cricket:** Rules & formats, Player statistics, Match summaries, Batting & bowling tactics
27. **Football:** Rules & competitions, Player analytics (xG), Match reports, Tactics & formations
28. **Other sports:** Tennis & badminton, Basketball & hockey, Athletics & running, Swimming & martial arts
29. **Gaming and esports:** Game mechanics, Competitive strategies, Game reviews, Esports tournaments
30. **Hobbies and creative activities:** Painting, Text-based photography, DIY crafts, Text-based music theory

### Category G — Business, economy, and commerce
31. **Economics:** Inflation & purchasing power, Supply & demand, Employment & wages, Economic growth
32. **E-commerce:** Online checkout, Pakistan E-Commerce catalog, Shipping logistics, Returns & refunds
33. **Small businesses and entrepreneurship:** Business ideas & TAM, Startup costs & budgeting, Customer acquisition, Operations
34. **Marketing and advertising:** Brand positioning, Advertising strategies (AIDA), Customer segmentation, Campaign analytics
35. **Jobs and careers:** Job descriptions, Resume & STAR interviews, Career planning, Professional skills

### Category H — Technology and digital life
36. **Websites and web services:** Usability heuristics, Information architecture, WCAG accessibility, Web performance
37. **Computers and operating systems:** Hardware microarchitectures, OS features & paging, Computer troubleshooting, Upgrades
38. **Smartphones and mobile apps:** Smartphone specs, Mobile app features, Battery degradation, Mobile usability
39. **Internet and computer networks:** Network terminology (OSI), Speed & latency, Wi-Fi troubleshooting, QoS reliability
40. **Artificial intelligence and data science:** Machine learning concepts, Data analysis, Applied AI, AI ethics & limitations

### Category I — Society, public services, and infrastructure
41. **Population and demographics:** Population growth, Age pyramids, Urbanization, Household composition
42. **Transportation and traffic:** Traffic congestion, Road safety, Public transport (BRT), Route navigation
43. **Emergencies and disaster preparedness:** Fire safety, Earthquake preparedness, Flood mitigation, Emergency response (ICS)
44. **Water and sanitation:** Drinking water quality, Water conservation, Wastewater aeration, Household water use
45. **Housing and buildings:** Rental lease features, Building materials, Energy efficiency, Maintenance planning

### Category J — Travel, communication, and human behavior
46. **Travel and tourism:** Destination descriptions, Travel budgeting, Accommodation comparisons, Traveler reviews
47. **Languages and communication:** WordNet semantics, Syntax trees, Translation equivalence, Written comprehension
48. **Human behavior and psychology:** Decision-making heuristics, Memory & attention, Motivation, Social group behavior
49. **Relationships and family life:** Family communication, Conflict resolution, Parenting styles, Interpersonal cooperation
50. **Non-political news and current events:** Science developments, Weather reports, Sports journalism, Public health notices

</details>

---

## 🔒 Provenance & Licensing

All datasets are licensed under established open terms:
- **CC-BY-SA 4.0:** Wikimedia Foundation encyclopedic and technical corpora.
- **MIT & Apache-2.0:** Hugging Face and GitHub academic ML benchmarks (MMLU, GSM8K, Hendrycks MATH, Pakistan E-Commerce).
- **Public Domain / CC0 1.0:** Project Gutenberg literature, OpenML labor relations database.
- **CC-BY 4.0:** Zenodo climate extremes research tutorials.
- **ODbL 1.0:** Open Data global gazetteer database.

No pirated film scripts, gated journal articles, or confidential personally identifiable information (PII) were collected.

---

## 👨‍💻 Maintainer & Attribution

Curated and maintained by **Muhammad Wasif** ([@Muhammad-Wasif](https://github.com/Muhammad-Wasif)).
For issues, contributions, or extensions, open an issue or pull request on GitHub!
