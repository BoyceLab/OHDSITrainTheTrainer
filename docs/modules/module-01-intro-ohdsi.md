# Module 01 · Introduction to OHDSI & OMOP: The Common Data Model and Standardized Vocabularies

!!! info "Program Context"
    This module launches the six-week **Train-the-Trainer Program** for analysts and engineers transitioning from Epic Clarity to the OMOP Common Data Model (CDM).  
    It introduces the OHDSI community, the OMOP CDM structure, and standardized vocabularies—the foundation for all later sessions.

---

## Pre-Readings
Before class, review the following chapters from the **Book of OHDSI**:

- **Chapter 4 – The Common Data Model**  
    4.1 Design Principles  
    4.2 Data Model Conventions  
    4.3 CDM Standardized Tables  
- **Chapter 5 – Standardized Vocabularies**  
    5.1 Why Vocabularies, and Why  
    5.2 Concepts  
    5.3 Relationships  
    5.4 Hierarchy  

*Links:* [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/) • [OHDSI Community](https://www.ohdsi.org/community/)  

---

## Learning Objectives – Week 1
- Understand the **OHDSI ecosystem** and the purpose of the OMOP CDM.  
- Explain **why standardized vocabularies matter** for reproducible analytics.  
- Navigate **Athena** to explore concept hierarchies and export concept IDs.  
- Build basic **concept sets** in Atlas and translate them into SQL pipelines.  

---

## Agenda / Topics (Approx. 4 hours)
| Segment | Duration | Description |
|----------|-----------|-------------|
| **Welcome & Introductions** | 15 min | Orientation to the six-week program and participant introductions |
| **Value Proposition Vignette** | 15 min | Demonstration of running an established phenotype from the OHDSI Phenotype Library |
| **Overview of OMOP CDM** | 30 min | History, design principles, standardized tables, and conventions |
| **Tour of Key Resources** | 20 min | Walk-through of this repo, Athena, Atlas, and CDM documentation pages |
| **Standardized Vocabularies & Concept Hierarchy** | 30 min | How concepts, relationships, and hierarchy link data domains |
| **Break** | 10 min | |
| **Guided Demonstrations** | 90 min |  • Exploring Athena  • Creating concept sets in Atlas  • Translating Atlas outputs into SQL queries |
| **Debrief & Homework Preview** | 10 min | Summary of key takeaways and assignment overview |

---

## Guided Exercise / Lab 1
**Goal:** Build and export a concept set for a real-world condition (e.g., diabetes, hypertension).  
**Steps:**  
1. Search for concepts and descendants in Athena.  
2. Create the same concept set in Atlas.  
3. Export concept IDs and use them in a sample SQL pipeline.  

**Deliverable:** Exported CSV of concept IDs uploaded to the class GitHub repo.

---

## Key Resources
- [Atlas Documentation](https://ohdsi.github.io/Atlas/)  
- [Athena Vocabulary Browser](https://athena.ohdsi.org/)  
- [EHDEN Academy](https://academy.ehden.eu/)  
- [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/)  

---

## Takeaways
- The OMOP CDM provides a **shared, scalable data model** for analytics.  
- Standardized vocabularies enable **semantic alignment** across data sources.  
- Concept sets built in Atlas feed **reproducible pipelines** for SQL or R.  

**Next:** Proceed to [Module 02 – Advanced Vocabularies and Concept Sets](module-02-cdm-vocabularies.md).
