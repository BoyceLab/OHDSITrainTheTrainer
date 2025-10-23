# OHDSI Train-the-Trainer Curriculum

## Overview and Format
This Train-the-Trainer program is a comprehensive two-day “boot camp” aimed at preparing trainers to teach the OHDSI (Observational Health Data Sciences and Informatics) framework to oncology researchers and clinicians. The curriculum combines live sessions (with recordings) and hands-on team exercises, supported by pre-course readings and asynchronous e-learning tracks. The emphasis is on real-world problem solving and observational epidemiology fundamentals in an oncology context. Trainers will learn not only OHDSI tools and methods, but also how to effectively teach these concepts to others.  

Key format features include:

- **Pre-class Preparation**: Participants complete curated pre-readings, watch introductory videos (e.g. an OHDSI overview from leadership), and take short knowledge quizzes before the live sessions.
- **Two-Day Intensive Boot Camp**: Interactive modules (~60–90 minutes each) combining lectures/demos with team-based exercises that mirror oncology research tasks (e.g. building a breast cancer cohort).
- **Integrated Multi-Persona Approach**: Sessions are integrated but accommodate different learner personas with examples and optional side exercises:
  - **Vocabulary Experts**: Focus on terminology mapping using OHDSI tools.
  - **Statisticians**: Emphasis on study design validity and minimal jargon.
  - **Data Scientists**: Optional SQL exercises and code-based Atlas outputs.
  - **Clinicians/Residents**: Fast, outcome-oriented Atlas workflows with minimal technical details.
- **Observational Epidemiology Thread**: Reinforce study design, bias, confounding, and cohort principles throughout.
- **Asynchronous Follow-Up**: Access to self-paced modules (e.g. EHDEN Academy) tailored to interests/personas, hosted on a MkDocs site with all materials.

By the end of the program, participants will master OHDSI’s tools and teaching strategies, culminating in a **capstone project** where trainees design and deliver a mock training session.

---

## Curriculum Modules Overview
Modules span two days, with oncology-focused examples (e.g. breast/lung cancer cohorts). No formal exams per module; comprehension is tested through exercises and the capstone.

### Module 0: Project Orientation and Onboarding
- **Format**: Asynchronous pre-work
- **Content**:
  - Project background & goals
  - Roles and responsibilities of trainers (“navigators”)
  - SOPs, resources, FAQs, contacts
  - Pre-reading, community orientation, and quiz
- **Persona considerations**: Equal relevance to all personas; ensures shared baseline.

### Module 1: Introduction to OHDSI and the OMOP Common Data Model
- **Topics**:
  - OHDSI background & mission
  - What is OMOP CDM and why use it
  - Real-world impact (e.g. multi-center oncology studies)
  - Overview of training program and resources
- **Persona considerations**: Different framing for statisticians, vocab experts, data scientists, and clinicians.

### Module 2: OMOP CDM Architecture and Standardized Vocabularies
- **Topics**:
  - CDM tables and relationships
  - Standard vocabularies (SNOMED, LOINC, RxNorm)
  - Use cases and vocabulary search demonstrations
  - Hands-on vocabulary exercise (HER2+ breast cancer cohort)
  - Oncology extension introduction (Episode tables)
- **Persona considerations**: Tailored engagement for technical vs. clinical learners.

### Module 3: Extract–Transform–Load (ETL) Processes into OMOP
- **Topics**:
  - ETL overview and challenges
  - OHDSI ETL tools (White Rabbit, Rabbit in a Hat, Usagi)
  - Hands-on mapping exercise with oncology data
  - Data anomalies and documentation practices
- **Persona considerations**: Vocabulary experts lead mapping, clinicians gain high-level understanding.

### Module 4: Data Quality and Consistency
- **Topics**:
  - Importance of quality checks
  - Kahn data quality framework
  - OHDSI tools: Data Quality Dashboard (DQD), Achilles
  - Common issues and oncology examples
  - Exercise: triage DQD/Achilles outputs
- **Persona considerations**: Each persona contributes different perspectives on quality.

### Module 5: Implementing Analytics Using OMOP – From Cohorts to Evidence
- **Topics**:
  - Study design primer (characterization, estimation, prediction)
  - OHDSI tools: Atlas and HADES
  - Network study workflow
  - Hands-on cohort building (oncology-focused)
  - Observational epidemiology concepts
  - Reproducibility and documentation
- **Persona considerations**: Exercises emphasize vocabulary, epi, code, or clinical intuition depending on persona.

### Module 6: Data Security, Privacy, and Compliance
- **Topics**:
  - Importance of privacy and security
  - Regulations: HIPAA, GDPR, others
  - OMOP’s role in de-identification
  - Governance and sensitive data handling
  - Exercise: addressing privacy concerns
- **Persona considerations**: Different emphasis (ethical duty for clinicians, technical safeguards for data scientists, etc.).

### Module 7: Building and Managing an OHDSI Project Team
- **Topics**:
  - Key roles (PM, ETL dev, vocabulary specialist, analyst, clinician SME)
  - Team collaboration practices (GitHub, Slack, Agile basics)
  - Managing timelines, troubleshooting
  - Exercise: site project management scenario
  - Training others and knowledge transfer
- **Persona considerations**: Builds leadership and communication skills across personas.

### Module 8: Advanced Topics and Emerging Trends
- **Topics**:
  - Advanced querying and ML applications
  - Oncology module deep dive
  - Interoperability with FHIR/i2b2
  - Unstructured data and NLP
  - Genomics, imaging, SDOH, wearables
  - Future OHDSI developments
- **Persona considerations**: Showcases possibilities for each learner type.

### Module 9: Train-the-Trainer Skills and Strategies
- **Topics**:
  - Adult learning techniques
  - Curriculum customization
  - Handling Q&A, mixed audiences, and clinician engagement
  - Using provided materials
  - Mentorship and evaluation
  - Exercise: microteaching
- **Persona considerations**: Focus on adjusting teaching style.

### Module 10: Capstone Project – Design a Training Session
- **Assignment**:
  - Design and deliver a short OHDSI training session
  - Develop objectives, materials, scenarios, engagement strategies
  - Present to group and receive feedback
- **Assessment**: Evaluates content knowledge and teaching effectiveness.

### Module 11: Wrap-Up, Evaluation, and Next Steps
- **Topics**:
  - Knowledge recap
  - Participant feedback
  - Certification and acknowledgments
  - Continued learning resources (forums, workgroups, Book of OHDSI, EHDEN Academy)
  - Community participation

### Module 12: Post-Training Refresher (3-Months Post-Course)
- **Topics**:
  - Case discussions and peer learning
  - Mini-refreshers for common challenges
  - Updates on new developments
  - Networking and ongoing community

---
!!! note "Reference Texts"
    - [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/)  
    - [OHDSI.org](https://www.ohdsi.org/who-we-are/)  
    - [Oncology Extension](https://ohdsi.github.io/CommonDataModel/oncology.html)  
    - [RWD Guide](https://rwd.guide/)  
