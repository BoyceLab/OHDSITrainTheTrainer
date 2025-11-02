# ✅ OHDSI Training: OMOP Vocabulary & SQL Exploration  
## Answer Key & Instructor Notes

---

## 🧩 Section 1: Concept Basics — Answers

1. **True or False:**  
   ✅ **True.**  
   Every data element in OMOP (diagnosis, procedure, drug, observation, measurement, etc.) is represented as a *concept* from a controlled vocabulary.

---

2. **Multiple Choice:**  
   ✅ **B.** A unique integer key assigned by OMOP for each concept.  
   The `concept_id` serves as the internal OMOP identifier and is not tied to source codes directly.

---

3. **Short Answer:**  
   ✅ **Standard concepts** are canonical OMOP representations used across all data sources for analysis.  
   **Non-standard concepts** are source-specific (e.g., ICD9, CPT) and must be mapped to standard ones via `concept_relationship`.

---

4. **Multiple Choice:**  
   ✅ **B.** `concept_relationship`  
   This table defines links between concepts (e.g., “Maps to”, “Is a”, “Subsumes”).

---

5. **True or False:**  
   ✅ **True.**  
   A `concept_name` can appear multiple times (e.g., “Diabetes mellitus” may appear across SNOMED, ICD9, and RxNorm with different IDs).

---

## 🧮 Section 2: Practical SQL Exercises — Sample Answers

> Results may vary depending on the vocabulary release (Athena version).  
> These are representative expected outcomes and explanations.

---

### Exercise 1 — Identify a Concept
```sql
SELECT concept_id, concept_name, vocabulary_id, domain_id, standard_concept
FROM concept
WHERE concept_name = 'Major depressive disorder';
