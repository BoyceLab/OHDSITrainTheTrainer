# OHDSI Train-the-Trainer Curriculum (6-Week Program)

> **Audience:** Data analysts/engineers (primarily Epic Clarity users) transitioning to the **OMOP Common Data Model (CDM)** and OHDSI toolchain.  
> **Format:** 6 weeks • 1 live session per week • **4 hours per session** (+ optional statisticians’ tracks).  
> **Goal:** Prepare trainers to confidently teach OMOP/OHDSI concepts and workflows, with emphasis on migration from Epic Clarity queries to OMOP-based analytics.

---

## Program Outcomes
By the end of the program, participants will be able to:
1. Explain the OMOP CDM and **Standardized Vocabularies**, and translate Epic Clarity data elements to OMOP domains/tables.
2. Build, evaluate, and share **concept sets** and perform vocabulary navigation at beginner → advanced levels.
3. Assess **data quality** using OHDSI tools and interpret findings for remediation.
4. Define and characterize **cohorts** in **ATLAS** and export results reproducibly.
5. Perform **CDM-aligned data extraction** using the **SEARCH** tool.
6. (Optional, statisticians) Execute **treatment pathway** analyses and apply **HADES** workflows for characterization/estimation/prediction.
7. Teach these topics effectively to mixed audiences (engineers, analysts, clinicians, statisticians).

---

## Logistics & Expectations
- **Live sessions (4h)** blend lecture, demos, and hands-on labs (approx. 40/60 split). Recordings provided.
- **Pre-work (1–2h/week)**: short readings/videos + setup tasks to maximize lab time.
- **Homework (1h/week)**: applied practice between sessions to reinforce learning. Homework is discussed at the start of each following session.
- **Team labs** are domain-agnostic and designed for reuse.
- **Repo & deliverables**: All slides, lab notebooks, queries, and instructor notes live in this GitHub repo.

---

## Access & Environment (Day 0)
**Goal:** Ensure everyone can access required systems and tools ahead of Week 1.

**Systems & Tools Checklist**
- **ATLAS** (read/write access to training environment)
- **OMOP CDM** read access to a small training database (synthetic or de-identified)
- **SEARCH** tool access (and permissions configured)
- **R (≥4.2)**, **RStudio** (or Posit Workbench), and ability to install OHDSI packages; optional **Python** if your site uses it
- **HADES** meta-package (optional, statisticians’ weeks)
- **Git & GitHub** (clone/pull/push repo; issues enabled)
- **SQL client** with read access (e.g., Databricks, DBeaver) for direct CDM inspection

**Day 0 Deliverables**
- Completed environment checklist (template provided)
- Test run: connect to CDM; open ATLAS; run a sample SEARCH query

---

## Weekly Schedule (High-Level)

| Day | Topic | Focus |
|---|---|---|
| **Day 0** | Environment Walk-through | Access, installs, permissions, smoke tests |
| **Day 1** | OMOP CDM + Intro to Standardized Vocabularies | From Epic Clarity to OMOP domains/tables & basic vocab |
| **Day 2** | Advanced Vocab, Concept Sets, Intro to Data Quality | Concept set best practices, advanced navigation, DQD/Achilles intro |
| **Day 3** | Cohort Definition & Characterization with ATLAS | Cohort design, characterization, reproducibility |
| **Day 4** | Data Extraction with the SEARCH Tool | Cohort-aware extraction and study packages |
| **Day 5** *(Optional)* | Treatment Pathway Analysis | For statisticians: pathways design/interpretation |
| **Day 6** *(Optional)* | Advanced Analytics with HADES | For statisticians: characterization, estimation, prediction |

> **Timebox:** Each live session is **4 hours (240 min)** with **one 10–15 minute break**.  
> **Homework:** Each week concludes with an ~**1 hour** assignment to reinforce concepts and prepare for the next module.

---

## Detailed Agendas, Labs & Homework

### Day 1 — Introduction to OHDSI, OMOP CDM & Standardized Vocabularies

**Learning Objectives**
- Describe the mission of OHDSI and the design principles of the OMOP CDM.  
- Explain the importance of standardized vocabularies and how concept hierarchies work.  
- Navigate Athena and Atlas to build basic concept sets and export concept IDs.

**Agenda (240 min)**
1. **Welcome & introductions** (10 min)  
2. **Phenotype Library vignette** (15 min)  
3. **OMOP CDM overview** (30 min)  
4. **Tour of resources** (20 min)  
5. **Standardized vocabularies & concept hierarchy** (30 min)  
6. **Break** (15 min)  
7. **Guided demonstrations: Athena + Atlas concept sets** (110 min)  
8. **Debrief & homework preview** (10 min)

**Artifacts**
- Slides; Lab 1 worksheet & answer key; “Clarity→OMOP Mapping Cheat Sheet”; exported concept set CSV.

**Homework (~1h)**
- Recreate one concept set from class using a different condition (e.g., hypertension). Export concept IDs and be ready to share on Day 2.

---

### Day 2 — Advanced Vocabulary, Concept Sets, & Intro to Data Quality

**Learning Objectives**
- Build robust concept sets (inclusion/exclusion, descendants, standard/non-standard handling).  
- Evaluate concept set coverage and drift; document intent for reusability.  
- Recognize data quality dimensions (conformance, completeness, plausibility) and the role of vocabularies in DQ.

**Agenda (240 min)**
1. **Concept set design patterns & pitfalls** (50 min)  
2. **Hands-on vocabulary drills** (40 min)  
3. **Break** (15 min)  
4. **Intro to DQD & Achilles** (40 min)  
5. **Lab 2: Build & validate concept sets** (75 min)  
6. **Interpreting DQ signals impacting cohort logic** (20 min)

**Artifacts**
- Concept set rubric; Lab 2 concept set bundle (CSV/JSON); DQ quick-start.

**Homework (~1h)**
- Run a DQD or Achilles summary on your training CDM (or sample data). Note three issues that could affect cohort building for discussion on Day 3.

---

### Day 3 — Cohort Definition & Characterization with ATLAS

**Learning Objectives**
- Translate clinical intent into cohort entry/exit logic and inclusion rules.  
- Use ATLAS to define cohorts and run characterization.  
- Export and version cohort definitions for reuse.

**Agenda (240 min)**
1. **Cohort design primer (index, washout, eras)** (40 min)  
2. **ATLAS demo: target & comparator cohorts** (40 min)  
3. **Break** (15 min)  
4. **Characterization & result interpretation** (35 min)  
5. **Lab 3: Build a phenotype & run characterization; commit exported JSON** (95 min)  
6. **Debrief & trainer facilitation tips** (15 min)

**Artifacts**
- Cohort design checklist; Lab 3 instructions; export/versioning guide.

**Homework (~1h)**
- Refine your cohort by adding an inclusion or exclusion rule. Re-run characterization and compare outputs to your original cohort.

---

### Day 4 — Data Extraction with the SEARCH Tool

**Learning Objectives**
- Perform cohort-aligned extractions using the SEARCH tool.  
- Parameterize pulls for counts, person-level datasets, and time-bounded windows.  
- Ensure extracts are reproducible and accompanied by cohort/concept definitions.

**Agenda (240 min)**
1. **SEARCH concepts & permissions** (30 min)  
2. **Query patterns (CDM domains, joins, cohort filters)** (50 min)  
3. **Break** (15 min)  
4. **Export formats & downstream use** (30 min)  
5. **Lab 4: Build an extraction spec; run & validate outputs** (95 min)  
6. **Packaging results with provenance** (20 min)

**Artifacts**
- Extraction spec template; validation checklist; sample outputs.

**Homework (~1h)**
- Using your Day 3 cohort, design and run a SEARCH extraction for patient-level data. Document query logic and output summary for Day 5.

---

### Day 5 *(Optional, Statisticians)* — Treatment Pathway Analysis

**Learning Objectives**
- Understand pathway cohort construction and sequencing rules.  
- Run pathway analyses and interpret visualizations.  
- Communicate caveats (data quality, censoring, competing risks) to non-statistical audiences.

**Agenda (240 min)**
1. **Pathways design & assumptions** (45 min)  
2. **Demo: running a treatment pathway workflow** (45 min)  
3. **Break** (15 min)  
4. **Lab 5: Generate pathways for a sample cohort** (100 min)  
5. **Interpreting & presenting findings** (35 min)

**Artifacts**
- Pathway parameter guide; presentation template.

**Homework (~1h)**
- Identify one pathway anomaly or insight from your lab results. Prepare a brief (3–5 slide) summary for Day 6.

---

### Day 6 *(Optional, Statisticians)* — Advanced Analytics with HADES

**Learning Objectives**
- Set up HADES and run characterization/estimation/prediction pipelines.  
- Explain confounding control, design diagnostics, and reproducibility.  
- Package study artifacts for peer review/network studies.

**Agenda (240 min)**
1. **HADES overview & setup** (40 min)  
2. **Characterization/Estimation/Prediction walkthroughs** (70 min)  
3. **Break** (15 min)  
4. **Lab 6: Execute an end-to-end analysis with diagnostics** (95 min)  
5. **Results packaging & trainer notes** (20 min)

**Artifacts**
- Starter study skeleton; diagnostic checklist.

**Homework (~1h)**
- Complete the HADES workflow on a small cohort of your choice and submit summary diagnostics. Be ready to discuss lessons learned during wrap-up.
