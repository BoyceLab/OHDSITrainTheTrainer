## Atlas Navigation Features

The left-hand navigation will direct your search for different analytic options (see **Figure 1**).

- **Home:** Permalink redirects you to the Atlas landing page.  
- **Data Sources:** Provides capability to review standardized reporting for each of the data sources configured for your Atlas environment. Here, review available populations and data sets. From select drop-down menus, select from any available observational database(s). Subsequently, select from any of the corresponding standardized reports available within the previously selected source.  
- **Search:** Enables you to search the OMOP standardized vocabularies, and understand and apply concepts within those vocabularies.  
- **Concept Sets:** Enables you to create your own set of codes that will be used throughout the standardized analyses. These sets can be saved and reused in all your analyses.  
- **Cohort Definitions:** Provides ability to construct a set of persons who satisfy one or more criteria for a duration of time, and these cohorts can serve as a basis of inputs for all subsequent analyses.  
- **Characterizations:** Allows you to look at one or more of your defined cohorts and summarizes characteristics about those patient populations in an analytic capability.  
- **Cohort Pathways:** Reviews the sequence of clinical events that occur within one or more populations.  
- **Incidence Rates:** Provides the ability to estimate the incidence of outcomes within target populations of interest.  
- **Profiles:** Explores an individual patient’s longitudinal observational data to summarize an individual’s situation.  
- **Estimation:** Conducts population-level effect estimation studies using a comparative cohort design. Comparisons between one or more target and comparator cohorts can be explored for a series of outcomes.  
- **Prediction:** Allows you to apply machine-learning algorithms to conduct patient-level prediction analyses.  
- **Jobs:** Details queries and analyses. This list displays jobs that are running in the background for long-running jobs or reports.  
- **Configuration:** Displays data sources configured in the source configuration; while it is not possible to edit configurations here, it is possible to review options for the sources of the data available.  
- **Feedback:** Provides a method to contact Atlas administration regarding issues with the database, features, or enhancements.

---

## Using Data Sources

The Data Sources feature provides capability to review standardized reporting for each of the data sources configured for your Atlas environment. From here, review available populations and data sets.

1. Select **Data Sources** in the left-hand navigation.
2. From the first drop-down menu, select a **Source**. This has been configured for your Atlas environment.
3. From the second drop-down menu, select a **Report**. This displays a series of standardized reports.

**Selecting the Report “Dashboard” will display:**

- The source name and number of persons within the database  
- Gender and age demographic charts  
- Cumulative observation graph displaying the amount of time observed in the database  
- Persons with Continuous Observation graph displaying the number of persons observed within a given month  

Hover a mouse over a chart element in the dashboard to display additional quantitative information.

Several reports from the drop-down menu present a series of graphs. For every graph, hover a mouse over a table or chart element to render a pop-up that displays additional details and information. Some Report elements display **Treemaps**. Treemap representation shows a number of boxes, the size of which represents the prevalence of a condition concept within the database and the color of which represents its intensity (by number of records per person who have that concept).

1. Hover over a box within the treemap to display a record’s detailed information.  
2. Click on a box within the treemap to load a drilldown report with additional information about prevalence, type, and age at first occurrence.

Next to the tab labeled **Treemap** is a tab for **Table**. Click the **Table** tab to represent the data in a tabular view (see **Figure 2**).

1. Click on a row of data to display additional information about the concept.  
2. Click the button **Show columns** to adjust which columns display.  
3. Click the button **Copy** to copy the concept information to your clipboard.  
4. Click the button **CSV** to export the information to an Excel spreadsheet.

**Figure 2: Visit Report, Table Tab**

Of the reports available under **Data Sources**:

- **Data Density:**  
  - A line report for every data domain supported  
  - A line report of records per person, enabling you to understand whether or not the data density seems to be growing as a function of the total data, or as a function of the amount of data per person  
  - A **Concepts per Person** line box plot, indicating distribution of distinct information per person across selected data domains  

- **Person:** Series of graphs including year of birth, gender, race, and ethnicity. These enable an overview of demographic distribution and potential data outliers.

- **Visit:** Treemap showing the prevalence and density of information associated with different types of visits within the data source. To search for a specific visit type, click **Table** and use the **Filter** box.

- **Condition Occurrence:** Treemap where box size represents prevalence and color intensity represents number of records per person. **Table** tab allows drilldown into concept prevalence over time, age information, and frequency of diagnosis. Use **Filter** to search.

- **Procedure:** Treemap showing prevalence and intensity of procedure concepts.

- **Drug Exposure:** Treemap showing prevalence and number of records per person the concept represents. Hover to display additional info (see **Figure 3**). Click a box to open a drilldown report of prevalence, type, and age at first occurrence.

  **Figure 3: Treemap, Drug Exposure (e.g., ibuprofen 400 MG)**

- **Drug Era:** Treemap of ingredients used in continuous persistence exposure (aggregated to ingredient level). Use **Treemap** or **Table**, and click concepts for a drilldown.

- **Measurement:** Treemap showing vitals, labs, and other measurements; **Table** for drilldown into prevalence over time, age information, and results. Use **Filter** to search.

> *(See OHDSI Data Sources Video Tutorial)*

---

## Using Search

The Search tool enables you to search the OMOP standardized vocabularies and understand and apply concepts within those vocabularies.

1. Select **Search** from the left-hand navigation.  
2. At the top, select the **Search** tab.  
3. In the **Search** field, enter words to find related concepts (e.g., “Migraine”). Results can be filtered using the left-hand filters (see **Figure 4**).

The search feature can query conditions, drugs, vitals, observations, procedures, devices, measurements, ICD-10 codes, etc.

**Figure 4: Search with Filters**

Click any line item to open a detailed vocabulary view with tabs:

- **Details**: Vocabulary ID, Concept ID, Concept Code, and other properties  
- **Related Concepts**: Broaden/narrow similar terms  
- **Hierarchies**: Parents/children in OMOP  
- **Record Counts**: Sources and quantities

Clicking a record navigates to **Concept Sets**.  
> *(See OHDSI Search Video Tutorial)*

---

## Using Concept Sets

The Concept Sets tool enables you to create your own set of codes used throughout standardized analyses. Concept sets are foundational to subsequent tools and analyses in Atlas.

1. Select **Concept Sets** in the left-hand navigation.  
2. Click an existing Concept Set to view Concept Names and Domains, with checkboxes for **Exclude**, **Descendants**, and **Mapped** (see **Figure 5**).

**Figure 5: Concept Set Expressions (example: COVID Concept Set)**

**Create a New Concept Set:**

1. From the **List** tab, click **New Concept Set**. Enter a title and click the green **Save** icon (see **Figure 6**).

**Figure 6: New Concept Set, Title and Beginning**

2. In the left-hand navigation, select **Search** (not the small search under the Concept Set tabs).  
3. Enter search terms; use filters (e.g., Standard Concept or Domain).  
4. Open a result and use **Hierarchy** to view parents/children.  
5. Click the shopping cart icon to add to the Concept Set (icon turns orange). You can add items to later exclude (see **Figure 7**).

**Figure 7: Concept Hierarchy, Adding Terms to New Concept Set**

6. Click the breadcrumb to return to your **New Concept Set** page.

In **Concept Set Expression**:

1. Use **Exclude** to exclude concepts.  
2. Use **Descendants** to include children.  
3. Click the green **Save** icon.

> *(See OHDSI Concept Sets Video Tutorial)*

---

## Using Cohort Definitions

The Cohort Definitions tool lets you construct a set of persons who satisfy criteria for a duration of time; these cohorts can serve as inputs for analyses.

1. Select **Cohort Definitions**.  
2. Click **New Cohort Definition**.

**Define the Cohort:**

1. Enter a title; click the green **Save**.  
2. Under **Cohort Entry Events**, **Add Initial Event** (see **Figure 8**).  
3. Choose an event (e.g., Drug Exposure), then **import concept** to pick from Concept Sets.  
4. Use drop-downs to specify date/sequence.  
5. **Add Attribute** (e.g., gender, first exposure, age) (see **Figure 8**).  
6. Click **Restrict initial events** when ready.

**Figure 8: Adding Cohort Entry Event to Cohort Set**

**Inclusion Criteria:**

1. Click **New Inclusion Criteria** and name it.  
2. **Add criteria to group** (criteria era, condition inclusion, device exposure, etc.).  
3. Remove items with **Delete Criteria**.  
4. Set **Cohort Exit** rules.  
5. Save.

**Other Tabs:**

- **Concept Sets:** Review used concepts.  
- **Generation:** Generate on a data source.  
- **Export:** View **Text**, **Graphical**, **JSON**, **SQL**; **Copy to Clipboard**.  
- **Messages:** Warnings/memos (yellow highlight when new).

At the top-right (see **Figure 9**):

- Green **Save**  
- Blue **X** (close)  
- Blue duplicate (copy)  
- Blue link (shareable permalink)  
- Red trash (delete)

**Figure 9: Cohort Definition Icons**

> *(See OHDSI Cohort Definitions Video Tutorial)*

---

## Using Characterizations

Characterizations summarize characteristics about one or more defined cohorts (cohort-level descriptive summary statistics from person-level covariate data).

1. Select **Characterizations**.  
2. Open an existing characterization or create new.

**Design Tab:**

1. Select one or more **Cohorts**.  
2. Under **Cohort Definitions**, **Import** definitions.  
3. Under **Feature analyses**, **Import** features; filter on the left; select all needed; **Import** (see **Figure 10**).

**Figure 10: Adding Feature Analyses to Characterizations**

**Executions:**

1. Go to **Executions**, choose a source, **Generate**, then **View Latest Result**.  
2. Use **Filter panel** to toggle cohorts (checkmarks), features, and domains (see **Figure 11**).

**Figure 11: Filtering Cohorts in Characterizations > Executions**

You can review **All Prevalence Covariates**, **Demographics**, and charts. Use **Export** to download sections to Excel.

> *(See OHDSI Characterizations Video Tutorial)*

---

## Using Cohort Pathways

Cohort Pathways reviews the sequence of clinical events that occur within one or more populations and generates aggregated transitions between event cohorts among patients in a target cohort.

1. Select **Cohort Pathways**.  
2. Open an existing analysis.

**Design Specification:**

1. **Target Cohorts:** **Import** from Cohort Definitions.  
2. **Event Cohorts:** **Import** from Cohort Definitions.  
3. Add as many as needed.  
4. **Analysis Settings:** set sequence parameters.

**Run & Review:**

1. Go to **Executions**; select a **Data Source**; **Generate** (revise settings if failures/timeouts).  
2. **View Latest Results**: a Target Cohort legend and a **sunburst plot** appear.  
   - Inner ring: first-line therapy  
   - Outer rings: subsequent/combo sequences  
3. Click items for detailed paths in the right panel.  
4. **Utilities** tab provides exportable code for sharing design specs.

> *(See OHDSI Cohort Pathways Video Tutorial)*

---

## Using Incidence Rates

Estimate the incidence of outcomes within target populations.

1. Select **Incidence Rates**.  
2. Open an existing analysis or **New Analysis**.

**Specify:**

1. **Target Cohorts** (at-risk population) and **Outcome Cohorts** (outcomes of interest).  
2. **Add Target Cohort** / **Add Outcome Cohort** via pop-up (remove with the **x** icon) (see **Figure 12**).

**Figure 12: Add and Remove Target Cohorts**

3. **Time At Risk:** define start/end relative to target cohort start/end.  
4. Optional **Study Window** (calendar date range).  
5. Optional **Stratify criteria** (e.g., `Gender=male`, `Age > 65`).

**Generation:**

1. Choose sources; **Generate**.  
2. Results include:  
   - Source name  
   - Number of persons  
   - Number of observed cases  
   - Incidence proportion  
   - Time at risk (person-years) and incidence rate  

**Reports:** Summary stats, stratification impact, treemap (box size = population proportion; color = incidence rate gradient).

Use green **Save** or blue **X** to close.  
> *(See OHDSI Incidence Rates Video Tutorial)*

---

## Using Profiles

Displays an individual patient’s longitudinal observational data.

1. Select **Profiles**.  
2. Choose database(s).  
3. Enter **Person ID** and press **Enter**.

**Display includes:**

- Patient demographics  
- Number of events  
- Data over time (day 0 = first observation)  
- Swimlane of timestamped clinical events (conditions, drugs, devices, observations, procedures, etc.)

Hover over dots for details.

**Explore:**

- Click-and-drag within a swimlane to zoom time.  
- Use **Domain Facet** filters on the left.  
- Use **Filter** on the right (between graph and table).

**Color-code:**

1. Click the blue **paintbrush** icon (see **Figure 13**).  
2. Search for a concept (e.g., “Lisinopril”).  
3. Select the concept and a color.  
4. Repeat for others (e.g., hypertension).  
5. Close the pop-up and review colored swimlanes.

**Figure 13: Patients Display Buttons**

Tabular data below the chart includes Concept ID, Concept Name, Domain, Start/End dates.  
> *(See OHDSI Profiles Video Tutorial)*

---

## Using Estimation

Conduct population-level effect estimation using a comparative cohort design.

1. Select **Estimation**.  
2. Click **New Population Level Effect Estimation**.

**Comparative Cohort Settings:**

1. **+ Add Comparison** to define target/comparator cohorts (and negative control outcomes).  
2. Use folder icons to select Cohort Definitions (see **Figure 14**).  
3. **Add Outcome** cohorts; select negative controls from Concept Sets.  
4. Include/exclude covariate Concept Sets.  
5. Return to landing page as needed.

**Figure 14: Adding Comparison Cohorts in Estimation Analyses**

**Effect Estimation Analysis Settings:**

1. **Study Population:** set dates and options.  
2. **Covariate Settings:** default recommended set; click to view/edit (see **Figure 15**).  
3. **Time At Risk:** define windows.  
4. **Propensity Score Adjustment:** configure (additional covariate settings, control settings, prior/LASSO).  
5. **Outcome Model Settings:** Logistic, Poisson, or Cox PH.

**Figure 15: Covariate Selection in Estimation**

**Evaluation Settings:** configure negative controls for empirical calibration.

**Utilities & Export:**

1. Review settings table.  
2. Name the study package and **Download** (R package `.zip`).  
3. **Export** JSON expression.  
> *(See OHDSI Video Tutorial for Estimation)*

---

## Using Prediction

Apply machine-learning algorithms for patient-level prediction.

1. Select **Prediction**.  
2. Click **New Patient Level Prediction**.

**Prediction Problem Settings:**

- Add **Target Cohort(s)** and **Outcome Cohort** from Cohort Definitions.

**Analysis Settings:**

- **+ Add Model Settings** (algorithm types).  
- **+ Add Covariate Settings** (predictors; check/uncheck features).  
- **+ Add Population Settings** (time at-risk and other criteria; e.g., new drug users with 1-year follow-up).

**Execution & Training Settings:**

- Define execution/training (model trains on a training set, then evaluates on a holdout set).

**Utilities & Results:**

- **Utilities** tab shows settings and allows **Download** of an R package; **Export** JSON (see **Figure 16**).  
- If errors occur, **Utilities** will describe them; return to **Specification** to adjust.

**Figure 16: Prediction Results**

> *(See OHDSI Video Tutorial for Prediction)*

---

## Using Jobs

Shows jobs running in the background for long-running jobs or reports.

- Select **Jobs** to see all jobs, status, runner, and timestamp.  
- **Refresh Jobs** (green button).  
- **CSV** (gray button) to download as an Excel spreadsheet.

---

## Using Configuration

Displays data sources configured in the source configuration.

- Select **Configuration** to view sources.  
- Editing is not possible here; edits must be done in the database.

---

## Using Feedback

Contact Atlas administration regarding issues, features, or enhancements.

- Select **Feedback** and follow instructions to submit issues.

---

## Frequently Asked Questions

**Q: Why are some features broken/not working?**  
Try switching web browsers. Google Chrome is the recommended browser for Atlas.

---

## OHDSI Video Tutorials

Explore the complete **[OHDSI Atlas Tutorials Playlist](https://www.youtube.com/playlist?list=PLpzbqK7kvfeUXjgnpNMFoff3PDOwv61lZ)** on YouTube.

---

### 📊 Using Data Sources
[![Using Data Sources](https://img.youtube.com/vi/Cueuvq0-xXc/0.jpg)](https://youtu.be/Cueuvq0-xXc)

### 🔍 Using Search
[![Using Search](https://img.youtube.com/vi/NI8urevLuqY/0.jpg)](https://www.youtube.com/watch?v=NI8urevLuqY)

### 🧩 Using Concept Sets
[![Using Concept Sets](https://img.youtube.com/vi/mfjxNwn3KkM/0.jpg)](https://youtu.be/mfjxNwn3KkM)

### 👥 Using Cohort Definitions
[![Using Cohort Definitions](https://img.youtube.com/vi/JQFGedOaNiw/0.jpg)](https://youtu.be/JQFGedOaNiw)

### 📈 Using Characterizations
[![Using Characterizations](https://img.youtube.com/vi/FU8DqF1mcDQ/0.jpg)](https://youtu.be/FU8DqF1mcDQ)

### 🔄 Using Cohort Pathways
[![Using Cohort Pathways](https://img.youtube.com/vi/rdniIztguys/0.jpg)](https://youtu.be/rdniIztguys)

### 📉 Using Incidence Rates
[![Using Incidence Rates](https://img.youtube.com/vi/sl1tkcNT17U/0.jpg)](https://youtu.be/sl1tkcNT17U)

### 👤 Using Profiles
[![Using Profiles](https://img.youtube.com/vi/_vSQQDBhXVg/0.jpg)](https://youtu.be/_vSQQDBhXVg)

### 📊 Using Estimation
[![Using Estimation](https://img.youtube.com/vi/YYxp3CDD-PE/0.jpg)](https://www.youtube.com/watch?v=YYxp3CDD-PE)

### 🤖 Using Prediction
[![Using Prediction](https://img.youtube.com/vi/qiTXEkLt7qs/0.jpg)](https://www.youtube.com/watch?v=qiTXEkLt7qs&list=PLpzbqK7kvfeUXjgnpNMFoff3PDOwv61lZ&index=19)

---


## Additional Resources

- OHDSI’s Atlas Wiki (permalink: <https://github.com/OHDSI/Atlas/wiki>)  
- Book of OHDSI (permalink: <https://ohdsi.github.io/TheBookOfOhdsi/>)  
- Athena Domain Wiki (permalink: <https://athena.ohdsi.org/search-terms/start>)

---

## Glossary of Terms

**Bias**  
The expected value of the error (the difference between the true value and the estimated value).

**Causal effect**  
What population-level estimation concerns itself with. One definition equates a “causal effect” as the average of the “unit-level causal effects” in a target population. The unit-level causal effect is the contrast between the outcome had an individual been exposed and the outcome had that individual not been exposed (or been exposed to A as against B).

**Characterization**  
Descriptive study of a cohort or entire database.

**Cohort**  
A set of persons who satisfy one or more inclusion criteria for a duration of time.

**Concept**  
A term (with a code) defined in a medical terminology (e.g., SNOMED CT).

**Concept set**  
An expression representing a list of concepts that can be used as a reusable component in various analyses.

**Common Data Model (CDM)**  
A convention for representing healthcare data that allows portability of analysis.

**Condition**  
A diagnosis, a sign, or a symptom, which is either observed by a provider or reported by the patient.

**Covariate**  
Data element (e.g., weight) used as an independent variable in a statistical model.

**Device**  
A foreign physical object or instrument used for diagnostic or therapeutic purposes beyond chemical action (e.g., pacemakers, stents, syringes, sutures, defibrillators, surgical materials).

**Drug**  
A biochemical substance formulated to exert a physiological effect when administered. Includes prescription/OTC medicines, vaccines, biologics (not radiological devices).

**Domain**  
Defines allowable Concepts for standardized fields in CDM tables (e.g., “Condition” domain concepts appear in CONDITION_OCCURRENCE tables).

**Matching**  
Method to create exposed/unexposed groups that are similar on measured characteristics.

**Measurement**  
A structured value obtained through systematic testing/examination.

**Measurement error**  
When a recorded measurement differs from the true measurement.

**Negative control**  
Exposure-outcome pair believed not to cause/prevent the outcome; used to assess method performance.

**Observation**  
A clinical fact about a person obtained via examination, questioning, or procedure.

**Observation period**  
Span of time a person is at risk to have clinical events recorded in source systems.

**Outcome**  
The focal event/condition for an analysis (e.g., stroke).

**Patient-level prediction**  
Predictive models producing patient-specific probabilities for future outcomes.

**Population-level estimation**  
Study into causal effects; estimates an average (population-level) effect size.

**Positive control**  
Exposure-outcome pair believed to cause/prevent the outcome; used to assess method performance.

**Procedure**  
Activity or process ordered/carried out by a provider for diagnostic/therapeutic purpose.

**Propensity score (PS)**  
Probability of receiving a treatment based on baseline covariates, often via logistic regression.

**Selection bias**  
Bias from differences between analyzed patients and the target population.

**Self-controlled designs**  
Designs comparing outcomes during different exposures within the same patient.

**Sensitivity analysis**  
Variant of the main analysis to assess impact of uncertain choices.

**Standard Concept**  
A valid concept allowed to appear in the CDM.

**Visit**  
Span of continuous medical services at a care site in a given setting.

**Vocabulary**  
A list of words/phrases with definitions or translations.

_All definitions derived from the Book of OHDSI (open source). See Standardized Vocabularies from OHDSI._

---

## Table of Figures

- **Figure 1:** Atlas Navigation  
- **Figure 2:** Visit Report, Table Tab  
- **Figure 3:** Treemap, Drug Exposure ibuprofen 400 MG  
- **Figure 4:** Search with Filters  
- **Figure 5:** Concept Set Expressions (COVID Concept Set)  
- **Figure 6:** New Concept Set, Title and Beginning  
- **Figure 7:** Concept Hierarchy, Adding Terms to New Concept Set  
- **Figure 8:** Adding Cohort Entry Event to Cohort Set  
- **Figure 9:** Cohort Definition Icons  
- **Figure 10:** Adding Feature Analyses to Characterizations  
- **Figure 11:** Filtering Cohorts in Characterizations > Executions  
- **Figure 12:** Add and Remove Target Cohorts  
- **Figure 13:** Patients Display Buttons  
- **Figure 14:** Adding Comparison Cohorts in Estimation Analyses  
- **Figure 15:** Covariate Selection in Estimation  
- **Figure 16:** Prediction Results
