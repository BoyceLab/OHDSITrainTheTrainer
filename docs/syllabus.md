# 📚 Syllabus — OHDSI Train-the-Trainer (6-Week Core + Optional Modules)

This master syllabus outlines **required readings and tools for the six-week Train-the-Trainer program**, followed by **optional advanced modules** for continued professional development.  
Use it to prepare before sessions, assign follow-ups afterward, or extend your learning beyond the core course.

---

## A) Core Six-Week Syllabus (Required)

> 💡 Tip: Chapters refer to the [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/).  
> For broader context on data sources and study design, see also the [RWD Guide](https://rwd.guide/).

| **Week / Day** | **Focus** | **Primary Readings / Viewings** | **Tools & Docs** | **Homework / Follow-up** |
|-----------------|------------|---------------------------------|------------------|---------------------------|
| **Day 0 – Environment Setup** | Verify access and installations | OHDSI.org – [Who We Are](https://www.ohdsi.org/who-we-are/) · OHDSI Forum “Introduce Yourself” | [Environment Checklist Template](../common_artifacts/environment-checklist-template.md) · ATLAS login · SQL client setup | Complete environment checklist · Test CDM connection and ATLAS login |
d ATLAS login |
| **Week 1 – OMOP CDM & Athena Vocabulary Exploration** | Understand CDM structure and vocabularies | *Book of OHDSI* Ch. 4 **The Common Data Model** (§ 4.1 Design Principles · 4.2 Data Model Conventions · 4.3 CDM Standardized Tables); Ch. 5 **Standardized Vocabularies** (§ 5.1 Why Vocabularies and Why · 5.2 Concepts · 5.3 Relationships · 5.4 Hierarchy) | [Athena Browser](https://athena.ohdsi.org/) · Example CDM ERD | Identify standard and non-standard concepts in Athena · Document mappings (`Maps to`, `Is a`, `Has ancestor`) |
| **Week 2 – Concept Sets in Atlas & Introduction to Data Quality Concepts** | Build concept sets in Atlas; explore data quality ideas | *Book of OHDSI* Ch. 4 (Data Quality Concepts) | Atlas Concept Sets · Overview of [Data Quality Dashboard](https://github.com/OHDSI/DataQualityDashboard) and **Achilles** (discussion only) | Create concept set for chosen condition and export CSV/JSON · Reflect on how vocabulary choices affect data quality |
| **Week 3 – Cohort Definition & Characterization with ATLAS** | Design and characterize cohorts | *Book of OHDSI* Ch. 19 (Study Steps) | ATLAS Cohort Editor · Characterization module | Refine cohort logic · Compare cohort characterization outputs |
| **Week 4 – Data Extraction with SEARCH** | Retrieve OMOP data for analysis | *Book of OHDSI* Ch. 3 (ETL Processes) | SEARCH Tool Guide · SQL client | Build and validate an extraction spec for your cohort |
| **Week 5 – Treatment Pathway Analysis (Optional)** | Sequence treatments and visualize pathways | *Book of OHDSI* Ch. 12 (Estimation) | ATLAS Pathways · Pathway Analysis docs | Generate pathway plots · Summarize a key insight (3–5 slides) |
| **Week 6 – Advanced Analytics with HADES (Optional)** | Characterization / Estimation / Prediction pipelines | *Book of OHDSI* Ch. 13 (Prediction) & Ch. 14 (HADES) | [HADES R Packages](https://ohdsi.github.io/Hades/) | Execute a small HADES workflow and report diagnostics |

---

## B) Optional / Advanced Modules (Beyond 6 Weeks)

These modules are not part of the six-week course but are available for self-study or site-specific customization.

| **Module #** | **Topic** | **Primary Readings** | **Key Tools / Docs** | **Optional Context / Use Case** |
|---------------|-----------|----------------------|----------------------|----------------------------------|
| **7. Team Building & Project Management** | Cross-functional OHDSI teamwork | *Book of OHDSI* Ch. 15 (Community) | GitHub Best Practices · Agile Boards | Managing multi-site collaborations |
| **8. Advanced Topics** | Machine learning, NLP, FHIR, unstructured data | *Book of OHDSI* Ch. 14 (HADES) | NOTE_NLP · FHIR mapping guides | Extending OMOP to AI and interoperability |
| **9. Train-the-Trainer Skills** | Adult learning and facilitation | Adult learning primers · Presentation skills | EXCELERATE TtT materials | Building your own institutional training program |
| **10. Capstone Project** | End-to-end practice study | Revisit Ch. 12, 13, 19 | ATLAS export → SQL / R | Present a mini network-style study |
| **11. Wrap-Up & Next Steps** | Sustaining engagement | *Book of OHDSI* Ch. 15 (Community) | OHDSI Workgroups Directory | Join or lead community workgroups |
| **12. Refresher (3-Month Post-Course)** | Review and updates | *Book of OHDSI* Ch. 19 (Study Steps) | Latest OHDSI release notes | Continuing learning & updates |

---

## C) Persona-Based Study Paths (Quick Reference)

| **Persona** | **Core Modules** | **Key Tools** | **Suggested Extras** |
|--------------|------------------|---------------|----------------------|
| **Vocabulary / Terminology Experts** | Weeks 1–3 | Athena · Atlas Concept Sets · Usagi | White Rabbit / Rabbit-in-a-Hat |
| **Statisticians / Design Analysts** | Weeks 4–6 (optional) | DQD (conceptual) · Atlas Pathways · HADES | RWD Guide (bias / confounding) |
| **Data Analysts/Data Scientists (SQL / R / Python)** | Weeks 2–6 | DatabaseConnector · FeatureExtraction · PatientLevelPrediction | Build reproducible pipelines in GitHub |
| **Clinicians / Analysts** | Weeks 1–3 | Atlas Cohort Editor | Explore Atlas characterization outputs for clinical plausibility |

---

## D) How to Use

- **Before class:** Read the listed chapters and preview tools for the upcoming week.  
- **During class:** Have the relevant tool (Athena or Atlas) open for guided demonstrations.  
- **After class:** Complete weekly homework and reflect on learnings.  
- **As a trainer:** Bookmark key OHDSI references for easy access:
  - [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/)  
  - [RWD Guide](https://rwd.guide/)  
  - [OHDSI Forums](https://forums.ohdsi.org/)  
  - [EHDEN Academy](https://academy.ehden.eu/)

---

*This syllabus supports the revised six-week OHDSI Train-the-Trainer program and provides a foundation for ongoing self-guided study.*
