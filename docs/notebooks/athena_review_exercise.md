# Week 2 · Athena Vocabulary Exploration Exercise

This exercise focuses exclusively on exploring the **OMOP Standardized Vocabularies** using [Athena](https://athena.ohdsi.org/).  
You’ll investigate how OMOP organizes concepts, relationships, and hierarchies — using *Type 2 Diabetes Mellitus* as an example condition.

---

## 💡 Learning Goals

By the end of this exercise, participants will be able to:

- Navigate **Athena** and locate clinical concepts across vocabularies.  
- Distinguish between **standard** and **non-standard** concepts.  
- Interpret concept **relationships** (“Maps to,” “Is a,” “Has ancestor,” etc.).  
- Recognize the structure and purpose of **OMOP vocabularies** and **domains**.  
- Understand how vocabulary choice impacts analytic consistency and data quality.

---

## 🔍 Section 1 – Getting Started with Athena

### Step 1.1 — Search for a Clinical Condition

1. Open [Athena](https://athena.ohdsi.org/).  
2. Search for **“Type 2 Diabetes Mellitus.”**  
3. Identify:  
   - The **standard concept** (shows `Standard Concept = S`).  
   - A related **non-standard concept** (`Standard Concept = NULL`).  
   - The **domain** (Condition, Measurement, Observation, etc.).  
   - The **vocabulary** source (SNOMED, ICD10CM, etc.).  
   - The **concept class** (Clinical Finding, Disorder, etc.).

![Athena search results](../assets/week2/athena-search.png)

#### Trainer Discussion Prompts

- What distinguishes “standard” vs. “non-standard” in OMOP?  
- Which vocabularies are most common for *Condition* domains?  
- Why are “mapping” relationships essential for standardization?

---

### Step 1.2 — Review Concept Details and Hierarchies

1. Open the **Concept Details** page for your chosen concept.  
2. Explore:  
   - **Relationships:** Which vocabularies map to this concept?  
   - **Ancestors / Descendants:** What broader or narrower concepts exist?  
   - **Concept Class:** What level of granularity does it represent?

![Athena concept details](../assets/week2/concept-details.png)

#### Trainer Discussion Prompts

- How do “Is a” and “Has ancestor” relationships define hierarchy?  
- Why might “Maps to” differ from “Is a”?  
- When reviewing descendants, how do you decide what’s “too specific” or unrelated?

---

## 🧭 Section 2 – Vocabulary Interpretation and Mapping Logic

### Step 2.1 — Explore Relationships

Choose a **non-standard ICD10CM** code for Type 2 Diabetes and inspect its mappings.

**Questions**

1. What happens if two ICD codes map to the same SNOMED concept?  
2. How does that improve cross-institution data consistency?  
3. When might “Maps to value” appear, and what does it mean?

![Athena relationships example](../assets/week2/athena-relationships.png)

---

### Step 2.2 — Vocabulary Hierarchy Practice

Pick another condition (e.g., *Hypertension*, *Asthma*, *Heart Failure*).

- Count how many **descendants** the top-level concept has.  
- Identify one or two that might be **too specific** (e.g., “Hypertension complicating pregnancy”).  
- Review the **vocabulary version** and note any updates.

#### Trainer Discussion Prompts

- How frequently are vocabularies updated in Athena?  
- What are the risks of using outdated vocabulary exports?  
- How can version metadata be stored for reproducibility?

---

## 🧪 Section 3 – Reflection and Data Quality Awareness

**Reflection Questions**

- How does using standardized vocabularies improve analytic reproducibility?  
- What are examples of mapping errors that could affect cohort counts?  
- How would you explain why non-standard codes can’t be used directly?  
- How does vocabulary hierarchy influence patient inclusion or exclusion?

#### Trainer Extension Discussion

- Explore a multi-domain concept like “HbA1c.”  
  - What differences appear across domains (Measurement vs Observation)?  
  - Why is correct domain assignment important for OMOP analytics?

---

## 📋 Deliverables

- Completed answers to all vocabulary questions.  
- 2–3 screenshots from Athena (search results, concept details, relationships).  
- Reflection notes summarizing key vocabulary and mapping insights.

---

## 🧾 Trainer Overview and Suggested Answers

Below are example responses and narrative explanations for discussion.

---

### Step 1.1 — Search for Type 2 Diabetes Mellitus

- **Standard concept:** `Type 2 diabetes mellitus` (SNOMED, Concept ID 201826, Domain = Condition).  
- **Non-standard concept:** `E11.9 – Type 2 diabetes mellitus without complications` (ICD10CM) → maps to SNOMED 201826.  
- **Domains:** Condition domain represents recorded diagnoses.  
- **Concept class:** Clinical Finding or Disorder.  
- **Vocabulary:** SNOMED (standard); ICD10CM (non-standard).  

**Explanation:**  
OMOP standardizes to SNOMED so that all EHRs reference a single shared meaning.  
ICD codes map to these SNOMED concepts through “Maps to” relationships in Athena.

---

### Step 1.2 — Concept Details and Hierarchies

- **Relationships:**  
  - *Maps to* connects non-standard to standard concepts.  
  - *Is a* and *Has ancestor* define hierarchical structure.  
- **Hierarchy Insight:**  
  *Type 2 diabetes mellitus* **is a** subtype of *Diabetes mellitus*.  
  Descendants include subtypes and complication variants (e.g., diabetic neuropathy).  

**Trainer Tip:**  
Encourage learners to decide which subtypes are clinically relevant for their purpose.

