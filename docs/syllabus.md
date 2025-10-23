# 📚 Syllabus — OHDSI Train-the-Trainer (6-Week Core + Optional Modules)

This master syllabus lists **required readings and tools for the six-week Train-the-Trainer program**, followed by **optional and advanced resources** for continued learning.  
Use it to prepare before sessions, assign follow-ups afterward, or extend your training beyond the core series.

---

## A) Core Six-Week Syllabus (Required)

> 💡 Tip: Chapters refer to the [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/).  
> See also the [Oncology Extension](https://ohdsi.github.io/CommonDataModel/oncology.html) and the [RWD Guide](https://rwd.guide/) for general methods on bias & confounding.

| **Week / Day** | **Focus** | **Primary Readings / Viewings** | **Tools & Docs** | **Homework / Follow-up** |
|-----------------|------------|---------------------------------|------------------|---------------------------|
| **Day 0 – Environment Setup** | Verify access and installations | OHDSI.org – [Who We Are](https://www.ohdsi.org/who-we-are/) · OHDSI Forum “Introduce Yourself” | Environment Checklist Template (`/common_artifacts/`) · ATLAS login · SQL client setup | Complete environment checklist · Test CDM connection and ATLAS login |
| **Week 1 – OMOP CDM & Athena Vocabulary Exploration** | Understand CDM tables and vocabularies | *Book of OHDSI* Ch. 4 **The Common Data Model** (§ 4.1 Design Principles · 4.2 Data Model Conventions · 4.3 CDM Standardized Tables); Ch. 5 **Standardized Vocabularies** (§ 5.1 Why Vocabularies and Why · 5.2 Concepts · 5.3 Relationships · 5.4 Hierarchy) | [Athena Browser](https://athena.ohdsi.org/) · Example CDM ERD | Identify standard and non-standard concepts in Athena · Document mappings (`Maps to`, `Is a`, `Has ancestor`) |
| **Week 2 – Concept Sets in Atlas & Intro to Data Quality** | Build concept sets · Intro DQ tools | *Book of OHDSI* Ch. 4 (Data Quality section overview) | Atlas Concept Sets · [Data Quality Dashboard](https://github.com/OHDSI/DataQualityDashboard) · Achilles | Create concept set for chosen condition and export CSV/JSON · Run mini DQD review |
| **Week 3 – Cohort Definition & Characterization with ATLAS** | Design and characterize cohorts | *Book of OHDSI* Ch. 19 (Study Steps) | ATLAS Cohort Editor · Characterization Module | Refine cohort logic · Compare characterization outputs |
| **Week 4 – Data Extraction with SEARCH** | Retrieve OMOP data for analysis | *Book of OHDSI* Ch. 3 (ETL Processes) | SEARCH Tool Guide · SQL client | Build and validate extraction spec for your cohort |
| **Week 5 – Treatment Pathway Analysis (Optional)** | Sequence treatments and visualize pathways | *Book of OHDSI* Ch. 12 (Estimation) | ATLAS Pathways · Pathway Analysis Docs | Generate pathway plots · Summarize an insight (3–5 slides) |
| **Week 6 – Advanced Analytics with HADES (Optional)** | Characterization / Estimation / Prediction pipelines | *Book of OHDSI* Ch. 13 (Prediction) & Ch. 14 (HADES) | [HADES R Packages](https://ohdsi.github.io/Hades/) | Execute small HADES study and report diagnostics |

---

## B) Optional / Advanced Modules (Beyond 6 Weeks)

These modules are **not part of the six-week live course** but remain available for self-study or institutional extensions.

| **Module #** | **Topic** | **Primary Readings** | **Key Tools / Docs** | **Optional Context or Use Case** |
|---------------|-----------|----------------------|----------------------|----------------------------------|
| **7. Team Building & Project Management** | Cross-functional team skills | *Book of OHDSI* Ch. 15 (Community) | GitHub Best Practices · Agile Boards | Managing multi-site collaborations |
| **8. Advanced Topics** | ML, NLP, FHIR, unstructured data | *Book of OHDSI* Ch. 14 (HADES) | NOTE_NLP · FHIR Mapping Notes | Extending OMOP to AI use cases |
| **9. Train-the-Trainer Skills** | Adult learning techniques | Adult learning primers · Presentation skills | EXCELERATE TtT materials | Designing your own training program |
| **10. Capstone Project** | Apply pipeline end-to-end | Revisit Ch. 12, 13, 19 | ATLAS export → SQL / R | Present a mini network study |
| **11. Wrap-Up & Next Steps** | Sustaining engagement | *Book of OHDSI* Ch. 15 (Community) | OHDSI Workgroups directory | Join community workgroups |
| **12. Refresher (3-Month Post-Course)** | Review and updates | *Book of OHDSI* Ch. 19 (Study Steps) | Latest release notes | Continuing education & community updates |

---

## C) Oncology-Specific Optional Readings

Supplementary resources for oncology-focused trainers and researchers using the OMOP Oncology Extension.

| **Reference** | **Citation / Link** |
|----------------|--------------------|
| *Extending the OMOP CDM and Standardized Vocabularies to Support Observational Cancer Research* | *JCO Clin Cancer Inform.* 2021 Jan; 5:12-20 [PMC8140810](https://pmc.ncbi.nlm.nih.gov/articles/PMC8140810/) |
| *A Scoping Review of OMOP CDM Adoption for Cancer Research Using Real-World Data* | *NPJ Digit Med.* 2025 Apr 7; 8(1):189 [PMC11973147](https://pmc.ncbi.nlm.nih.gov/articles/PMC11973147/) |
| OHDSI Oncology Working Group | [GitHub Repository](https://github.com/OHDSI/OncologyWG) · [Bladder Cancer Study](https://github.com/OHDSI/OncologyWG/wiki/Bladder-Cancer-Study) · [Oncology Tutorial](https://github.com/OHDSI/OncologyWG/wiki/Oncology-Tutorial) |
| OHDSI 2020 Talks – Rimma Belenkaya & Asieh Golozar | [OHDSI YouTube Playlist](https://www.youtube.com/@OHDSI) · [Ensuring Data Fitness for Oncology Research (2025)](https://www.youtube.com/watch?v=9-wB6e8Op7k) |

---

## D) Persona-Based Study Paths (Quick Reference)

| **Persona** | **Core Modules** | **Key Tools** | **Suggested Extras** |
|--------------|------------------|---------------|----------------------|
| **Vocabulary / Terminology Experts** | Weeks 1–3 | Athena · Atlas Concept Sets · Usagi | White Rabbit / Rabbit-in-a-Hat · Oncology Extension |
| **Statisticians / Design Analysts** | Weeks 4–6 (opt.) | DQD · Atlas Pathways · HADES | RWD Guide (bias / confounding) |
| **Data Scientists (SQL / R / Python)** | Weeks 2–6 | DatabaseConnector · FeatureExtraction · PatientLevelPrediction | Build reproducible pipelines with GitHub |
| **Clinicians / Residents** | Weeks 1–3 | Atlas Cohort Editor | Explore Atlas characterization for clinical plausibility |

---

## E) How to Use

- **Before class:** Read the “Primary Readings” and preview tools for the upcoming week.  
- **During class:** Have Athena or Atlas open for guided demonstrations.  
- **After class:** Complete homework and optional readings to reinforce learning.  
- **As a trainer:** Bookmark key references for quick access:  
  - [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/)   
  - [OHDSI Forums](https://forums.ohdsi.org/)  
  - [EHDEN Academy](https://academy.ehden.eu/)
  - [RWD Guide](https://rwd.guide/) 

---
