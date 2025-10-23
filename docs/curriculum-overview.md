# OHDSI Train‑the‑Trainer Curriculum (6‑Week Program)

> **Audience:** Data analysts/engineers (primarily Epic Clarity users) transitioning to the **OMOP Common Data Model (CDM)** and OHDSI toolchain.  
> **Format:** 6 weeks • 1 live session per week • **4 hours per session** (+ optional statisticians’ tracks).  
> **Goal:** Prepare trainers to confidently teach OMOP/OHDSI concepts and workflows, with emphasis on migration from Epic Clarity queries to OMOP‑based analytics.

---

## Program Outcomes
By the end of the program, participants will be able to:
1. Explain the OMOP CDM and **Standardized Vocabularies**, and translate Epic Clarity data elements to OMOP domains/tables.
2. Build, evaluate, and share **concept sets** and perform vocabulary navigation at beginner → advanced levels.
3. Assess **data quality** using OHDSI tools and interpret findings for remediation.
4. Define and characterize **cohorts** in **ATLAS** and export results reproducibly.
5. Perform **CDM‑aligned data extraction** using the **SEARCH** tool.
6. (Optional, statisticians) Execute **treatment pathway** analyses and apply **HADES** workflows for characterization/estimation/prediction.
7. Teach these topics effectively to mixed audiences (engineers, analysts, clinicians, statisticians).

---

## Logistics & Expectations
- **Live sessions (4h)** blend lecture, demos, and hands‑on labs (approx. 40/60 split). Recordings provided.
- **Pre‑work (1–2h/week)**: short readings/videos + setup tasks to maximize lab time.
- **Team labs** domain‑agnostic enough for broader reuse.
- **Repo & deliverables**: All slides, lab notebooks, queries, and instructor notes live in this GitHub repo.

---

## Access & Environment (Day 0)
**Goal:** Ensure everyone can access required systems and tools ahead of Week 1.

**Systems & Tools Checklist**
- **ATLAS** (read/write access to training environment)
- **OMOP CDM** read access to a small training database (synthetic or de‑identified)
- **SEARCH** tool access (and permissions configured)
- **R (≥4.2)**, **RStudio** (or Posit Workbench), and ability to install OHDSI packages; optional **Python** if your site uses it
- **HADES** meta‑package (optional, statisticians’ weeks)
- **Git & GitHub** (clone/pull/push repo; issues enabled)
- **SQL client** with read access (e.g., Databricks, DBeaver) for direct CDM inspection

**Day 0 Deliverables**
- Completed environment checklist (template provided)
- Test run: connect to CDM; open ATLAS; run a sample SEARCH query

---

## Weekly Schedule (High‑Level)

| Day | Topic | Focus |
|---|---|---|
| **Day 0** | Environment Walk‑through | Access, installs, permissions, smoke tests |
| **Day 1** | OMOP CDM + Intro to Standardized Vocabularies | From Epic Clarity to OMOP domains/tables & basic vocab |
| **Day 2** | Advanced Vocab, Concept Sets, Intro to Data Quality | Concept set best practices, advanced navigation, DQD/Achilles intro |
| **Day 3** | Cohort Definition & Characterization with ATLAS | Cohort design, characterization, reproducibility |
| **Day 4** | Data Extraction with the SEARCH Tool | Cohort‑aware extraction and study packages |
| **Day 5** *(Optional)* | Treatment Pathway Analysis | For statisticians: pathways design/interpretation |
| **Day 6** *(Optional)* | Advanced Analytics with HADES | For statisticians: characterization, estimation, prediction |

> **Timebox:** Each live session is 4 hours (with 2 short breaks). See detailed agendas below.

---

## Detailed Agendas & Labs

### Day 1 — OMOP CDM & Intro to Standardized Vocabularies
**Learning Objectives**
- Articulate why OMOP standardization matters for internal and multi‑site analytics.
- Map common **EHR entities** to OMOP domains (e.g., **Procedures → PROCEDURE_OCCURRENCE**, **Diagnoses → CONDITION_OCCURRENCE**, **Labs → MEASUREMENT**, **Medications → DRUG_EXPOSURE**, **Visits → VISIT_OCCURRENCE/DETAIL**).
- Navigate OMOP vocab structures (concepts, concept_relationship, domains, standard vs. source).

**Agenda (4h)**
1. Welcome & orientation to the 6‑week series (5-10m)
2. Introduction review (put in chat and intructor review (5-10m)
3. OMOP CDM overview & table tour (30m)
4. Intro to Standardized Vocabularies (SNOMED, RxNorm, LOINC) (50m)
5. Break (10m)
6. Lab 1: “From Source to OMOP” mapping scavenger hunt (60m): *Given commonly used items (e.g., ICD diagnosis code, lab test, medication), locate the OMOP standard concepts & destination tables in Athena.*
7. Debrief, trainer tips, and intro to homework assignment (10m)
    
**Artifacts**: Slides, Lab 1 worksheet & answer key, quick‑ref “Clarity→OMOP cheat sheet”.

---

### Day 2 — Advanced Vocabulary, Concept Sets, & Intro to Data Quality
**Learning Objectives**
- Build robust **concept sets** (inclusion/exclusion, descendant logic, standard/non‑standard handling).
- Evaluate concept set coverage and drift; document intent for reusability.
- Recognize data quality dimensions (conformance, completeness, plausibility) and the role of vocabularies in DQ.

**Agenda (4h)**
1. Concept set design patterns & pitfalls (60m)
2. Hands‑on vocabulary drills (45m)
3. Break (10m)
4. Intro to **Data Quality Dashboard (DQD)** & **Achilles** (45m)
5. Lab 2: Build & validate concept sets for a target condition and exposures (60m)
6. Interpreting DQ signals that affect cohort logic (20m)

**Artifacts**: Concept set rubric, Lab 2 concept set bundle (CSV/JSON), DQ quick‑start.

---

### Day 3 — Cohort Definition & Characterization with ATLAS
**Learning Objectives**
- Translate clinical intent into cohort entry/exit logic and inclusion rules.
- Use **ATLAS** to define cohorts and run **characterization**.
- Export and version cohort definitions for reuse in the repo.

**Agenda (4h)**
1. Cohort design primer (index, washout, eras) (45m)
2. ATLAS demo: building target & comparator cohorts (45m)
3. Break (10m)
4. Characterization & result interpretation (40m)
5. Lab 3: Build a phenotype & run characterization; commit exported JSON to Git (80m)
6. Debrief & trainer facilitation tips (20m)

**Artifacts**: Cohort design checklist, Lab 3 instructions, export/versioning guide.

---

### Day 4 — Data Extraction with the SEARCH Tool
**Learning Objectives**
- Perform **cohort‑aligned extractions** using the SEARCH tool.
- Parameterize pulls for counts, person‑level datasets, and time‑bounded windows.
- Ensure extracts are reproducible and accompanied by cohort/concept definitions.

**Agenda (4h)**
1. SEARCH concepts & permissions (30m)
2. Query patterns (CDM domains, joins, cohort filters) (60m)
3. Break (10m)
4. Export formats & downstream use (40m)
5. Lab 4: Build an extraction spec for a cohort; run and validate outputs (90m)
6. Packaging results with provenance (10m)

**Artifacts**: Extraction spec template, validation checklist, sample outputs.

---

### Day 5 *(Optional, Statisticians)* — Treatment Pathway Analysis
**Learning Objectives**
- Understand pathway cohort construction and sequencing rules.
- Run pathway analyses and interpret visualizations.
- Communicate caveats (data quality, censoring, competing risks) to non‑statistical audiences.

**Agenda (4h)**
1. Pathways design & assumptions (45m)
2. Demo: running a treatment pathway workflow (45m)
3. Break (10m)
4. Lab 5: Generate pathways for a sample cohort (90m)
5. Interpreting & presenting findings (50m)

**Artifacts**: Pathway parameter guide, presentation template.

---

### Day 6 *(Optional, Statisticians)* — Advanced Analytics with HADES
**Learning Objectives**
- Set up **HADES** and run characterization/estimation/prediction pipelines.
- Explain confounding control, design diagnostics, and reproducibility to trainees.
- Package study artifacts for peer review/network studies.

**Agenda (4h)**
1. HADES overview & setup (40m)
2. Characterization/Estimation/Prediction walkthroughs (70m)
3. Break (10m)
4. Lab 6: Execute a small end‑to‑end analysis with diagnostics (90m)
5. Results packaging & trainer notes (30m)

**Artifacts**: Starter study skeleton, diagnostic checklist.

---
