# Missing Subtopics & Download Failure Audit Report

## 1. Subtopic Coverage Audit

- **Total Required Subtopics:** 200
- **Successfully Downloaded Subtopics:** 200 / 200
- **Unmet or Missing Subtopics:** **0 (Zero)**

Every single one of the 200 subtopics enumerated in Section 11 has been researched, verified, and supplied with at least one downloadable, authentic, legally usable dataset stored in a separate, subtopic-specific folder.

## 2. Documented Platform Limitations & Excluded Candidates

In accordance with Section 1, Section 5 (Step 8), and Section 13, all candidate platforms or queries that encountered external access boundaries are recorded below with their exact technical causes and resolutions:

| Candidate & URL | Platform | Failure Category | Technical Reason | Verified Resolution |
|---|---|---|---|---|
| **Kaggle Auth Boundary**<br>[https://www.kaggle.com/datasets/zusmani/pakistani-dramas-and-movies-reviews-dataset](https://www.kaggle.com/datasets/zusmani/pakistani-dramas-and-movies-reviews-dataset) | Kaggle | `403 Forbidden / Login Wall` | Kaggle API requires private credentials (`kaggle.json`) and session tokens; direct anonymous HTTP downloads are blocked by platform policy. | Preserved verified Wikimedia Pakistani Dramas and Drama Subtitles GitHub repositories as authoritative open alternatives. |
| **World Bank API Read Timeout**<br>[https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD](https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD) | World Bank Open Data | `HTTPSConnectionPool Read Timeout (>10s)` | Direct World Bank REST endpoints encountered upstream connection drops and socket timeouts during automated fetches. | Utilized verified GitHub open macroeconomic GDP datasets from the frictionless data repository. |
| **UCI Machine Learning API Timeout**<br>[https://archive.ics.uci.edu/api/dataset?id=2](https://archive.ics.uci.edu/api/dataset?id=2) | UCI ML Repository | `HTTPSConnectionPool Read Timeout (>5s)` | Automated query throttling on UCI REST v1 interface prevented synchronous file streaming. | Sourced equivalent verified academic ML benchmarks via Hugging Face and GitHub research mirrors. |
| **Proprietary Academic Paywalls**<br>[https://www.sciencedirect.com/](https://www.sciencedirect.com/) | Elsevier / ScienceDirect | `Institutional Paywall / Access Boundary` | Full-text scientific journals are restricted under institutional subscription terms. | Substituted open-access peer-reviewed abstracts and Wikimedia Foundation scientific compendia. |
| **Multimedia Video Datasets**<br>[https://www.youtube.com/](https://www.youtube.com/) | YouTube / Video Portals | `Non-Text Excluded` | Video stream files violate the text-only requirement of Section 3A. | Collected text transcripts, dialogue corpora, and episodic metadata exclusively. |

## 3. Engineering Recommendations for Extended Scaling

1. **Kaggle Ingestion:** For data teams seeking to include Kaggle-exclusive user kernels, provision an official `~/.kaggle/kaggle.json` token with authenticated `kaggle datasets download` CLI execution.
2. **Institutional Academic Gateways:** Researchers seeking paywalled medical journals should route programmatic collectors through institutional EZproxy / Shibboleth gateways with publisher licensing agreements.
