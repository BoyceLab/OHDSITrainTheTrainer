# 🧠 OMOP SQL Examples for Databricks / DBeaver

This guide provides **SQL examples for exploring and validating OMOP CDM data** using your preferred SQL environment (Databricks, DBeaver, PostgreSQL client, etc.).  
Use during **Weeks 2–4** of the OHDSI Train-the-Trainer program to connect Atlas outputs to the underlying OMOP tables.

> ⚙️ Adapt schema names (e.g., `omop.`) to match your local setup. These examples assume read access to an OMOP training database.

---

## 1️⃣ Explore the CDM Structure

### List OMOP tables in your schema
```sql
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema ILIKE '%omop%';
```

### Count records across key tables
```sql
SELECT 'PERSON' AS table, COUNT(*) AS row_count FROM omop.person
UNION ALL
SELECT 'CONDITION_OCCURRENCE', COUNT(*) FROM omop.condition_occurrence
UNION ALL
SELECT 'DRUG_EXPOSURE', COUNT(*) FROM omop.drug_exposure
UNION ALL
SELECT 'MEASUREMENT', COUNT(*) FROM omop.measurement
UNION ALL
SELECT 'VISIT_OCCURRENCE', COUNT(*) FROM omop.visit_occurrence;
```

---

## 2️⃣ Vocabulary Lookups (Athena Alignment)

### Search for a condition
```sql
SELECT concept_id, concept_name, domain_id, vocabulary_id, standard_concept, concept_class_id
FROM omop.concept
WHERE LOWER(concept_name) LIKE '%diabetes%'
ORDER BY standard_concept DESC;
```

### Check relationships for one concept
```sql
SELECT cr.concept_id_1 AS source_concept,
       c1.concept_name AS source_name,
       cr.relationship_id,
       cr.concept_id_2 AS related_concept,
       c2.concept_name AS related_name
FROM omop.concept_relationship cr
JOIN omop.concept c1 ON c1.concept_id = cr.concept_id_1
JOIN omop.concept c2 ON c2.concept_id = cr.concept_id_2
WHERE cr.concept_id_1 = 201826  -- Example: Type 2 Diabetes Mellitus
ORDER BY cr.relationship_id;
```

### Find descendants
```sql
SELECT c.concept_id, c.concept_name, c.domain_id
FROM omop.concept_ancestor ca
JOIN omop.concept c ON ca.descendant_concept_id = c.concept_id
WHERE ca.ancestor_concept_id = 201826
ORDER BY c.concept_name;
```

---

## 3️⃣ Validate Atlas Concept Sets

### Check exported concepts from Atlas
```sql
SELECT c.concept_id, c.concept_name, c.domain_id, c.vocabulary_id, c.standard_concept
FROM omop.concept c
WHERE c.concept_id IN (201826, 319835, 2006877);
```

### Confirm that all are standard
```sql
SELECT COUNT(*) FILTER (WHERE standard_concept = 'S') AS standard_count,
       COUNT(*) AS total_count
FROM omop.concept
WHERE concept_id IN (201826, 319835, 2006877);
```

---

## 4️⃣ Cohort Definition Exploration (Atlas → SQL)

### Find patients meeting condition criteria
```sql
SELECT person_id,
       condition_concept_id,
       condition_start_date,
       condition_end_date
FROM omop.condition_occurrence
WHERE condition_concept_id IN (201826, 319835);
```

### Add visit context
```sql
SELECT co.person_id,
       co.condition_concept_id,
       v.visit_start_date,
       v.visit_concept_id
FROM omop.condition_occurrence co
JOIN omop.visit_occurrence v ON co.visit_occurrence_id = v.visit_occurrence_id
WHERE co.condition_concept_id IN (201826, 319835);
```

---

## 5️⃣ Validate SEARCH / Atlas Extractions

### Reproduce cohort counts manually
```sql
SELECT COUNT(DISTINCT person_id) AS patient_count
FROM omop.condition_occurrence
WHERE condition_concept_id IN (201826, 319835);
```

### Compare across visit types
```sql
SELECT v.visit_concept_id,
       COUNT(DISTINCT co.person_id) AS patients
FROM omop.condition_occurrence co
JOIN omop.visit_occurrence v ON co.visit_occurrence_id = v.visit_occurrence_id
WHERE co.condition_concept_id IN (201826, 319835)
  AND co.condition_start_date >= DATE '2015-01-01'
GROUP BY v.visit_concept_id;
```

---

## 6️⃣ Explore Data Quality Concepts

### Identify unmapped concepts
```sql
SELECT c.vocabulary_id,
       COUNT(*) AS unmapped_count
FROM omop.concept c
WHERE c.standard_concept IS NULL
GROUP BY c.vocabulary_id
ORDER BY unmapped_count DESC;
```

### Check completeness of a domain table
```sql
SELECT COUNT(*) AS total_conditions,
       COUNT(DISTINCT person_id) AS distinct_patients,
       COUNT(*) FILTER (WHERE condition_start_date IS NULL) AS missing_start_dates
FROM omop.condition_occurrence;
```

---

## ✅ Pro Tip: Align Atlas and SQL Outputs
1. In Atlas, click **Export → SQL** for your concept set or cohort.  
2. Run the SQL in Databricks or DBeaver.  
3. Compare row counts or sample IDs with Atlas results.  
4. Save both Atlas exports and SQL outputs for reproducibility evidence.

---

## 📘 References
- [Book of OHDSI – Common Data Model](https://ohdsi.github.io/TheBookOfOhdsi/CommonDataModel.html)  
- [Book of OHDSI – Standardized Vocabularies](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html)  
- [Book of OHDSI – Data Quality Concepts](https://ohdsi.github.io/TheBookOfOhdsi/DataQuality.html)

---

*Use these examples during Weeks 2–4 to practice validating Atlas logic and exploring OMOP data with your existing SQL skills.*
