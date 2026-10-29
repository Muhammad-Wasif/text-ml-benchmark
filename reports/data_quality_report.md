# Data Quality, Structure & Schema Audit Report

## 1. File Format Distribution

| Format | Dataset Count | Usage Description |
|---|---|---|
| **ARFF** | 1 | Structured records, encyclopedic extractions, or benchmark rows |
| **CSV** | 1 | Structured records, encyclopedic extractions, or benchmark rows |
| **JSON** | 199 | Structured records, encyclopedic extractions, or benchmark rows |
| **JSONL** | 1 | Structured records, encyclopedic extractions, or benchmark rows |
| **TXT** | 1 | Structured records, encyclopedic extractions, or benchmark rows |
| **ZIP** | 1 | Structured records, encyclopedic extractions, or benchmark rows |

## 2. Textual Richness and Linguistic Scope

- **Exclusively Text-Based:** Every single dataset preserved in the repository contains meaningful natural language text (articles, QA pairs, examination problems, product listings, gazetteer descriptions, technical guidelines, or literature). Pure numerical matrices without descriptive labels or text were strictly excluded.
- **Preservation of Source Idiosyncrasies:** In accordance with Section 3B, spelling, punctuation, capitalization, domain-specific vernaculars (e.g., Urdu transliterations in Pakistani dramas, regional SKU descriptions in Pakistani e-commerce, cricket terminology in match recaps) were preserved exactly as supplied by the upstream publishers.
- **Language Suitability:** The corpus is primarily English (`en`), incorporating bilingual and transliterated South Asian corpora where culturally authentic.

## 3. Content Field Auditing

Key detected text fields across typical domains:
- **Education & Exam Revision (MMLU / GSM8K):** `question`, `choices`, `answer`
- **Geography & Demographics (mledoze countries):** `name`, `capital`, `region`, `subregion`, `demonym`
- **Academic Performance (Student Habits CSV):** `Extracurricular Activities`, `Sleep Hours`, `Sample Question Papers Practiced`
- **E-Commerce & Retail (Pakistan E-Commerce):** `item_id`, `category_name_1`, `status`, `price`
- **General Domain Knowledge (Wikimedia Foundation):** `title`, `extract`, `pageid`
- **Labor Bargaining (OpenML Labor ARFF):** `wage-increase`, `cost-of-living-allowance`, `pension`, `education-allowance`
- **Classic Literature (Project Gutenberg):** Raw continuous unencumbered literary prose lines
