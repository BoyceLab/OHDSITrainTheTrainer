# OHDSI Train-the-Trainer Curriculum (6-Week Program)

> **Audience:** Data analysts/engineers (primarily Epic Clarity users) transitioning to the **OMOP Common Data Model (CDM)** and OHDSI toolchain.  
> **Format:** 6 weeks • 1 live session per week • **4 hours per session** (+ optional statisticians’ tracks).  
> **Goal:** Prepare trainers to confidently teach OMOP/OHDSI concepts and workflows, emphasizing the migration from Epic Clarity queries to OMOP-based analytics.

---

## Program Outcomes
By the end of the program, participants will be able to:

1. Explain the OMOP CDM and **Standardized Vocabularies**, translating Epic Clarity data to OMOP domains/tables.  
2. Build, evaluate, and share **concept sets** and perform vocabulary navigation at beginner → advanced levels.  
3. Assess **data quality concepts** using OHDSI frameworks and interpret findings.  
4. Define and characterize **cohorts in ATLAS** and export reproducible results.  
5. Perform **CDM-aligned data extraction** using the **SEARCH tool**, validating logic in familiar SQL clients.  
6. *(Optional)* Execute **treatment pathway** and **HADES analytics** workflows.  
7. Teach these topics effectively to mixed audiences (engineers, analysts, clinicians, statisticians).

---

## Logistics & Expectations
- **Live sessions (4 h)** blend lecture, demos, and hands-on labs (≈ 40 / 60 split).  
- **Pre-work (1–2 h/week):** short readings + setup tasks.  
- **Homework (≈ 1 h/week):** applied practice between sessions (reviewed at start of next week).  
- **Team labs** are domain-agnostic and reusable.  
- **Repo & deliverables:** All slides, lab files, SQL snippets, and instructor notes live in this GitHub repo.

---

## Access & Environment (Day 0)
**Goal:** Ensure all participants have access to required systems before Week 1.

**Systems & Tools Checklist**
- **ATLAS** (read/write training access)  
- **OMOP CDM** read access (synthetic or de-identified)  
- **SEARCH** tool (if available)  
- **R (≥ 4.2)** + RStudio / Posit Workbench (with OHDSI packages)  
- **Git & GitHub** (clone/pull/push repo)  
- **SQL Client** (e.g., Databricks, DBeaver) with OMOP read access  
- *(Optional)* **HADES meta-package** (for statistical weeks)

**Day 0 Deliverables**
- Complete environment checklist  
- Successfully connect to CDM, open ATLAS, and run a sample query

---

## Weekly Schedule (High-Level)

| Week | Topic | Focus |
|------|-------|-------|
| **Day 0** | Environment Walk-through | Access, installs, permissions, smoke tests |
| **Week 1** | OMOP CDM + Athena Vocabulary Exploration | Understand CDM tables and navigate vocabularies in Athena |
| **Week 2** | Concept Sets in Atlas + Intro to Data Quality Concepts | Build concept sets and relate Atlas outputs to SQL validation |
| **Week 3** | Cohort Definition & Characterization with ATLAS | Cohort design and SQL exploration in Databricks/DBeaver |
| **Week 4** | Data Extraction with SEARCH and SQL Validation | Cohort-aligned extraction + cross-checking with SQL clients |
| **Week 5 *(Opt.)*** | Treatment Pathway Analysis | For statisticians: pathway design and interpretation |
| **Week 6 *(Opt.)*** | Advanced Analytics with HADES | For statisticians: characterization, estimation, prediction |

> **Timebox:** Each session = 4 hours (240 min) with one 10–15 min break.  
> **Homework:** ≈ 1 hour per week to reinforce learning and prepare for the next session.

---

## Detailed Agendas, Labs & Homework

### Week 1 — OMOP CDM & Athena Vocabulary Exploration

**Learning Objectives**
- Understand OMOP CDM design principles and standardized vocabulary structure.  
- Map Epic Clarity data elements to OMOP domains (Condition, Procedure, Measurement).  
- Explore Athena concepts, relationships, and hierarchies.

**Agenda (240 min)**
1. Welcome & orientation (10 min)  
2. OMOP CDM overview (40 min)  
3. Athena basics – concept lookup & relationships (45 min)  
4. Break (15 min)  
5. Guided Athena exploration exercise (100 min)  
6. Debrief & homework preview (30 min)

**Artifacts**
- Slides; Lab worksheet; “Clarity → OMOP Mapping” cheat sheet; Athena screenshots.

**Homework (~1 h)**
- Choose a clinical condition (e.g., Type 2 Diabetes or Hypertension) and:  
  - Identify standard and non-standard concepts in Athena.  
  - Document `Maps to`, `Is a`, and `Has ancestor` relationships.  
  - Prepare screenshots and notes for Week 2 discussion.

---

### Week 2 — Concept Sets in Atlas & Introduction to Data Quality Concepts

**Learning Objectives**
- Build concept sets in Atlas using Athena concepts.  
- Export and validate concept set logic in SQL clients (Databricks/DBeaver).  
- Explore data quality concepts (conformance, completeness, plausibility) conceptually.

**Agenda (240 min)**
1. Review Week 1 Athena findings (15 min)  
2. Concept set design patterns & pitfalls (40 min)  
3. Atlas demo – creating concept sets (45 min)  
4. Break (15 min)  
5. Hands-on Lab 2 – build concept sets + export SQL (90 min)  
6. Validate concept sets in Databricks/DBeaver (25 min)  
7. Discuss data quality dimensions (10 min)

**Artifacts**
- Concept set rubric; Lab 2 export bundle (CSV/JSON); sample SQL validation queries.

**Homework (~1 h)**
- Using your Atlas concept set:  
  - Export SQL and run in Databricks or DBeaver.  
  - Record row counts and any unexpected results.  
  - Reflect on how vocabulary mappings influence data quality.

---

### Week 3 — Cohort Definition & Characterization with ATLAS and SQL Exploration

**Learning Objectives**
- Translate clinical intent into cohort entry/exit criteria and inclusion rules.  
- Use Atlas to define cohorts and run characterization.  
- Export cohort SQL and trace logic in Databricks/DBeaver.

**Agenda (240 min)**
1. Cohort design primer (index, washout, eras) (40 min)  
2. Atlas demo – target & comparator cohorts (40 min)  
3. Break (15 min)  
4. Lab 3 – build a phenotype & run characterization (90 min)  
5. SQL exploration – trace cohort logic in Databricks/DBeaver (40 min)  
6. Debrief & trainer discussion (15 min)

**Artifacts**
- Cohort design checklist; Lab 3 instructions; cohort SQL examples; export/version guide.

**Homework (~1 h)**
- Export your cohort SQL from Atlas and annotate key joins and filters in your SQL client.  
- Identify OMOP tables driving entry and exit criteria.

---

### Week 4 — Data Extraction with SEARCH and SQL Validation

**Learning Objectives**
- Perform cohort-aligned extractions using the SEARCH tool.  
- Review and validate extraction SQL in Databricks or DBeaver.  
- Document query logic and provenance for reproducibility.

**Agenda (240 min)**
1. SEARCH concepts & permissions (30 min)  
2. Query patterns across CDM domains (45 min)  
3. Break (15 min)  
4. Lab 4 – build an extraction spec & run outputs (90 min)  
5. SQL validation exercise in Databricks/DBeaver (45 min)  
6. Debrief (15 min)

**Artifacts**
- Extraction spec template; validation checklist; sample output summaries.

**Homework (~1 h)**
- Re-run your SEARCH extraction SQL manually in your SQL client.  
- Compare counts and summaries with Atlas/SEARCH results.

---

### Week 5 *(Optional, Statisticians)* — Treatment Pathway Analysis

**Learning Objectives**
- Understand pathway cohort construction and sequencing rules.  
- Run pathway analyses and interpret visualizations.  
- Communicate findings and limitations.

**Agenda (240 min)**
1. Pathways design & assumptions (45 min)  
2. Demo – running a treatment pathway workflow (45 min)  
3. Break (15 min)  
4. Lab 5 – generate pathways for a sample cohort (100 min)  
5. Interpret & present findings (35 min)

**Artifacts**
- Pathway parameter guide; presentation template.

**Homework (~1 h)**
- Identify one pathway insight from your analysis.  
- Prepare a 3–5 slide summary for Week 6.

---

### Week 6 *(Optional, Statisticians)* — Advanced Analytics with HADES

**Learning Objectives**
- Set up HADES and run characterization/estimation/prediction pipelines.  
- Explain confounding control and diagnostic outputs.  
- Package study artifacts for peer review.

**Agenda (240 min)**
1. HADES overview & setup (40 min)  
2. Characterization/Estimation/Prediction walk-through (70 min)  
3. Break (15 min)  
4. Lab 6 – execute end-to-end analysis with diagnostics (95 min)  
5. Results packaging & discussion (20 min)

**Artifacts**
- Starter study skeleton; diagnostic checklist.

**Homework (~1 h)**
- Complete a HADES workflow on a small cohort.  
- Submit summary diagnostics and lessons learned for wrap-up.
