# 🧠 OHDSI Training: OMOP Vocabulary & SQL Exploration  
## Homework / Exercise Set

---

### 📘 Learning Objectives
By completing this exercise, you should be able to:
- Understand how OMOP concepts are structured and standardized.  
- Distinguish between standard and non-standard concepts.  
- Write SQL queries to explore concept definitions and relationships.  
- Use OMOP tables (`concept`, `concept_relationship`) effectively.  

---

## 🧩 Section 1: Concept Basics — Quiz

1. **True or False:**  
   Every data value in the OMOP Common Data Model is represented as a *concept*.

2. **Multiple Choice:**  
   The `concept_id` column in the OMOP vocabulary tables represents:  
   A. The identifier from the original source vocabulary (e.g., ICD9 code)  
   B. A unique integer key assigned by OMOP for each concept  
   C. The domain name (Condition, Drug, etc.)  
   D. The relationship between two concepts  

3. **Short Answer:**  
   What is the key difference between a *standard* and *non-standard* concept?

4. **Multiple Choice:**  
   Which OMOP table can you query to determine how one concept maps to another?  
   A. `concept`  
   B. `concept_relationship`  
   C. `concept_ancestor`  
   D. `concept_synonym`

5. **True or False:**  
   A single `concept_name` may correspond to multiple rows in the `concept` table.

---

## 🧮 Section 2: Practical SQL Exercises

> 💡 Use the **OMOP vocabulary tables** (`concept`, `concept_relationship`, `concept_ancestor`) in your sandbox or training environment.  
> These queries are platform-agnostic and work with Athena vocabulary tables.

---

### Exercise 1 — Identify a Concept  
Use SQL to find all entries in the `concept` table with the name **"Major depressive disorder"**.  

**Questions:**  
a) How many rows are returned?  
b) Which have `standard_concept = 'S'`?  
c) What are the `vocabulary_id` and `domain_id` values?

```sql
SELECT concept_id, concept_name, vocabulary_id, domain_id, standard_concept
FROM concept
WHERE concept_name = 'Major depressive disorder';
```

---

### Exercise 2 — Find a Concept by Source Code  
Suppose you have the ICD-9 code **296.3**.  
Query the `concept` table to see how this code is represented in OMOP.  

**Question:**  
Is it a standard or non-standard concept?

```sql
SELECT concept_id, concept_name, standard_concept, vocabulary_id
FROM concept
WHERE concept_code = '296.3';
```

---

### Exercise 3 — Map a Non-Standard Concept to Its Standard Equivalent  
Using the `concept_id` you found in Exercise 2, find its standard mapping.

```sql
SELECT *
FROM concept_relationship
WHERE concept_id_1 = <nonstandard_id>
  AND relationship_id = 'Maps to';
```

**Questions:**  
- What is the standard concept_id?  
- What vocabulary does the standard concept belong to?  
- Why is using the standard concept important?

---

### Exercise 4 — Explore Relationships Between Concepts  
Pick a standard concept of interest (e.g., *Major depressive disorder* or *Hypertension*).  
Use the following query to explore all relationships it has with other concepts:

```sql
SELECT cr.relationship_id, c.concept_name AS related_concept, c.domain_id
FROM concept_relationship cr
JOIN concept c
  ON cr.concept_id_2 = c.concept_id
WHERE cr.concept_id_1 = <your_standard_concept_id>;
```

**Questions:**  
- What types of relationships appear (e.g., “Is a”, “Subsumes”)?  
- Which relationships might be useful when defining a concept set?

---

### Exercise 5 — Challenge Query: Concept Hierarchy
Find all **descendant concepts** for the standard concept *Hypertension* using `concept_ancestor`.  

```sql
SELECT descendant_concept_id, c.concept_name
FROM concept_ancestor a
JOIN concept c
  ON a.descendant_concept_id = c.concept_id
WHERE ancestor_concept_id = <hypertension_id>;
```

**Questions:**  
- How many descendant concepts exist?  
- Which ones seem clinically relevant?  

---

## 🧾 Section 3: Reflection

1. Why does OMOP use *standardized* vocabularies rather than native source codes?  
2. What are potential risks of using non-standard concepts in analyses?  
3. How can concept relationships influence your inclusion/exclusion criteria when building cohorts?  
4. How would you document your concept mappings for reproducibility?

---

## 🏁 Deliverable
Submit a short document (or notebook) that includes:
- Your SQL queries  
- A short explanation of each result  
- A paragraph summarizing what you learned about standardization and concept relationships  
