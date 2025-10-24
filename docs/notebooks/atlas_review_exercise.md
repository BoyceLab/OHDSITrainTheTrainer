# OHDSI Week 2 Exercise — Introduction to Atlas

> **Goal:** Hands-on exploration using the **Atlas** tool to build a cohort definition composed of multiple concept sets related to **Type 2 Diabetes Mellitus (T2DM)**.

---

## 🔗 Accessing Atlas

The Atlas tool can be accessed from within your **SAFE Desktop** environment using the link below:  
**[Launch Atlas Tool](XXXXLINK)**  

!!! note
    You must be inside **XXXXENVIRONMENT** (secure workspace) to access Atlas.  
    External or unapproved network connections will not work.

---

## 🧭 Learning Objectives

By the end of this exercise, you will be able to:

1. Navigate the Atlas interface and create a **new cohort definition**.  
2. Build **concept sets** for clinical definitions using OMOP Standardized Vocabularies.  
3. Apply filters and interpret **record counts (RC)** and **descendant record counts (DRC)**.  
4. Save, review, and validate a cohort definition.

---

## 🧩 Background

We are exploring how to define **Type 2 Diabetes Mellitus (T2DM)** using the **OHDSI Atlas** tool.  
There are multiple ways to identify patients who may have diabetes. For this course, we’ll focus on three approaches:

A. Having a **laboratory measurement** (e.g., HbA1c, fasting glucose, or random glucose) that suggests diabetes.  
B. Having a **diagnosis** of Type 2 Diabetes and **not** Type 1 Diabetes.  
C. Being prescribed a **medication** for glycemic control.

In each case, we’ll search for and select OMOP concept IDs to include in our cohort definition.  
For clinical accuracy, we’ll reference the **PheKB (Phenotype KnowledgeBase)** project:  
- Paper: [PheKB: a catalog and workflow for creating electronic phenotype algorithms for transportability](https://pubmed.ncbi.nlm.nih.gov/27026615/)  
- Website: [https://phekb.org](https://phekb.org)

---

## 🧱 Initialize Your Workbook

Before you begin:

1. Enter your **student_id** in the workbook cell below.
2. Press **Ctrl + Enter** to save your ID.
3. Verify that your environment is connected to the secure data source.

---

## 🧮 Create a New Cohort Definition

We’ll continue the work from the **Athena exercise** by exploring concept IDs and creating new concept sets.

### Steps

1. Open **Atlas** → select **Cohort Definitions** (left navigation).  
2. Click **New Cohort Definition** (top right).  
3. Name your cohort:  
   ```
   T2DM_[studentID]
   ```
   Example: `T2DM_jdoe01`
4. Click the green **Save** icon.  
5. Confirm that your cohort is saved and visible in your cohort list.

!!! note
    You can create and edit **Concept Sets** directly within your new cohort definition.

---

## 🧪 Concept Set 1 — Hemoglobin A1c Measurement

### Objective
Create a **concept set** for HbA1c measurements.

### Steps
1. Inside your cohort definition, click the **Concept Sets** tab.  
2. Click **New Concept Set** → name it `HbA1c Measurement`.  
3. Scroll down → click **Add Concepts**.  
4. In the search field, type **“Hemoglobin A1c”** → click the **blue magnifying glass** icon.  
5. Apply filters:
   - Vocabulary: **LOINC**
   - Class: **Lab test**
   - Domain: **Measurement**
   - Standard Concept: **Standard**
   - Invalid Reason: **Valid**
6. Sort by **RC (Record Count)** in descending order.

### Questions
- How many concepts have a **nonzero record count**?
- Which **OMOP concept ID** has the highest count?

Add your answers below:
```text
Answer 1:
Answer 2:
```

7. Select all relevant concepts using the **checkboxes**.  
8. Add **concept ID 3007263** (per PheKB guidance, even if RC=0).  
9. Click **Add To Concept Set**.  
10. Return to your cohort definition → click **Save**.  
11. Confirm the **HbA1c Concept Set** now includes 4 concepts.  
12. Optionally, click **Descendants** checkmarks (redundant here).  
13. Save the cohort again.

✅ **Result:** Your first concept set is complete!

---

## 🧪 Concept Set 2 — Fasting Glucose Measurement

### Objective
Define fasting glucose measurements.

### Steps
1. From your cohort, open the **Concept Sets** tab → click **New Concept Set**.  
2. Name it `Fasting Glucose Measurement`.  
3. Go to **Search** (left panel).  
4. Type **“Fasting Glucose”** → click **Search (magnifying glass)**.  
5. Apply filters (same as before).  
6. Sort by **RC** in descending order.  

### Questions
- What is the **concept ID** with nonzero count?
- What is the **record count (RC)** for that concept?

Add your answers:
```text
Answer 3:
Answer 4:
```

7. Select the concept(s) → click **Add To Concept Set**.  
8. Return to your cohort → **Save**.  
9. Confirm the concept set includes **1 concept**.  
10. Optionally, click **Descendants** checkmarks.  
11. Save again.

✅ **Result:** Your fasting glucose concept set is created.

---

## 🧪 Concept Set 3 — Random Glucose Measurement

### Objective
Define random (non-fasting) glucose measurements.

### Steps
1. From your cohort → **Concept Sets** → **New Concept Set**.  
2. Name it `Random Glucose Measurement`.  
3. Go to **Search** → type **“Glucose”**.  
4. Apply filters:
   - Vocabulary: **LOINC**
   - Class: **Lab test**
   - Domain: **Measurement**
   - Standard Concept: **Standard**
   - Invalid Reason: **Valid**
5. Sort by **RC** in descending order.

### Questions
- How many concepts have **nonzero rows**?
- Which two concept IDs correspond to **PheKB’s definition**?

Add your answers:
```text
Answer 5:
Answer 6:
```

6. Select **concept IDs 3004501 and 3000483**.  
7. Add to concept set.  
8. Save and verify that **2 concepts** are included.  
9. Optionally, check **Descendants**.  
10. Save cohort.

✅ **Result:** Random glucose measurement concept set complete.

---

## 💾 Wrap-Up

You have now:
- Created a new cohort definition (`T2DM_[studentID]`)
- Defined and saved three concept sets:
  - **HbA1c Measurement**
  - **Fasting Glucose Measurement**
  - **Random Glucose Measurement**
- Practiced searching, filtering, and reviewing record counts in Atlas.

!!! tip
    Save screenshots of your **Cohort Definition** and **Concept Sets** tabs.  
    These will be helpful for Week 4’s data extraction and validation steps.

---

## 📘 Reference Materials

- **PheKB Phenotyping Resource:** [https://phekb.org](https://phekb.org)
- **Book of OHDSI:** [https://ohdsi.github.io/TheBookOfOhdsi/](https://ohdsi.github.io/TheBookOfOhdsi/)
- **OHDSI Atlas Wiki:** [https://github.com/OHDSI/Atlas/wiki](https://github.com/OHDSI/Atlas/wiki)
- **Atlas Video Tutorials:** [YouTube Playlist](https://www.youtube.com/playlist?list=PLpzbqK7kvfeUXjgnpNMFoff3PDOwv61lZ)

---
