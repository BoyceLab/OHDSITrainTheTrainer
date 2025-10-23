# 🧑‍🏫 Trainer Guide — OMOP SQL Examples (Databricks / DBeaver)

This guide provides **expected results, interpretation notes, and discussion prompts** for the OMOP SQL examples.  
Use it during **Weeks 2–4** to help participants connect Atlas logic to the OMOP CDM and bridge GUI ↔ SQL understanding.

---

## 1️⃣ Explore the CDM Structure

**Expected Results**
- ~20–25 OMOP tables.  
- PERSON: 10–100k rows.  
- CONDITION_OCCURRENCE & DRUG_EXPOSURE largest tables.

**Discussion Prompts**
- Which OMOP tables resemble Epic Clarity structures?  
- Why separate visits, conditions, and drugs into unique domains?

---

## 2️⃣ Vocabulary Lookups (Athena Alignment)

**Expected Results**
- 50–100 diabetes-related concepts.  
- SNOMED entries marked `standard_concept = 'S'`; ICD entries `NULL`.  
- Concept 201826 → Type 2 Diabetes Mellitus.

**Trainer Notes**
- Reinforce that SNOMED is the standard for conditions.  
- Show ICD → SNOMED mapping through `concept_relationship`.

**Discussion**
> “What are the tradeoffs between precision (ICD detail) and standardization (SNOMED hierarchy)?”

---

## 3️⃣ Validate Atlas Concept Sets

**Expected Results**
- `standard_count = total_count` means all concepts are valid.  
- Non-standard results indicate incomplete mapping.

**Teaching Tip**
- Show how Atlas-generated SQL mirrors these queries.  
- Encourage using SQL validation before team submission.

---

## 4️⃣ Cohort Definition Exploration (Atlas → SQL)

**Expected Results**
- 10–100 matched rows per concept ID.  
- Adding visit join shows smaller counts (filtered by visit linkage).

**Trainer Tips**
- Encourage annotation of joins (`visit_occurrence_id`, `person_id`).  
- Use example to discuss cohort entry vs inclusion logic.

---

## 5️⃣ Validate SEARCH / Atlas Extractions

**Expected Results**
- Counts align within ±1–2% of Atlas results.  
- Differences due to null handling or observation period restrictions.

**Trainer Guidance**
- Show how to debug WHERE clauses and observation windows.  
- Reinforce habit of comparing manual SQL results to Atlas output.

---

## 6️⃣ Explore Data Quality Concepts

**Expected Results**
- <5% unmapped codes; <1% missing dates.  
- Discuss local vocabularies as frequent unmapped cases.

**Discussion**
> “Why should data engineers periodically recheck unmapped concept rates?”  
> “How can missing dates propagate bias into time-based analytics?”

---

## 🧩 Integration with Atlas

**Teaching Flow**
1. Export SQL from Atlas.  
2. Run it in SQL client.  
3. Compare and interpret results with cohort metadata.

**Trainer Quote**
> “Atlas automates SQL logic — validating that logic builds transparency and reproducibility.”

---

## 🧠 Summary Table

| Concept | Example Result | Key Teaching Point |
|----------|----------------|--------------------|
| Standard vs Non-standard | SNOMED = Standard; ICD = Non-standard | Always use standard concepts |
| Descendant Expansion | Adds subtypes | Broadens recall; needs review |
| Cohort SQL | SELECT + JOIN | Atlas builds reproducible SQL logic |
| Unmapped Codes | <5% | Indicates vocabulary completeness |

---

*Each SQL validation step reinforces analysts’ ability to bridge OMOP tools and their SQL comfort zone.*
