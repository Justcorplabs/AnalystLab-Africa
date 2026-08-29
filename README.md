# JustCorp Labs - Data Science Internship Portfolio (AnalystLab Africa)

This repository contains multiple internship projects completed as part of the AnalystLab Africa Data Science Internship and Experience Lab Programme.

1. **Employee Attrition Analysis** (Weeks 1-3) - a solo project analysing the IBM HR Analytics dataset.
2. **HealthConnect Experience Lab** (Week 4 onwards) - a shared cross-track project, contributed to from the Data Science track's perspective.

---

# Project 1: Employee Attrition Analysis

## Data Science Internship Project

This part of the repository contains a multi-week employee attrition project based on the **IBM HR Analytics - Employee Attrition & Performance** dataset.

The project progresses from exploratory analysis in Week 1, through feature engineering and machine-learning preprocessing in Week 2, to advanced statistical analysis and feature refinement in Week 3.

---

## Dataset

- **1,470 employees**
- **35 original variables**
- Target: `Attrition`
- **237 employees left**
- **1,233 employees remained**
- Overall attrition rate: **16.12%**
- No missing values
- No duplicate rows

---

## Week 1 - Business Understanding & Exploratory Data Analysis

Week 1 focused on understanding employee attrition patterns and translating them into business insights.

### Analysis included

- Data quality assessment
- Exploratory Data Analysis (EDA)
- Descriptive statistics
- Employee segmentation
- Correlation analysis
- Chi-square tests
- Welch's t-tests
- Overtime x Job Role interaction analysis
- Business Travel x Department interaction analysis
- Data visualisation
- Business recommendations
- Limitations and ethical considerations

### Key findings

- Overall attrition was **16.12%**.
- Employees working overtime had substantially higher observed attrition.
- Frequent business travellers experienced higher attrition.
- Attrition varied across job roles and departments.
- Employees who left were generally younger, earned less, and had shorter organisational tenure.
- Interaction analysis showed that overtime and travel-related attrition patterns differed across roles and departments.

These findings describe associations and do not establish causation.

---

## Week 2 - Feature Engineering & Data Preprocessing

Week 2 prepares the same dataset for machine-learning model development.

### Preprocessing performed

- Duplicate and missing-value validation
- Removal of constant variables:
  - `EmployeeCount`
  - `Over18`
  - `StandardHours`
- Removal of identifier:
  - `EmployeeNumber`
- Binary target encoding
- Feature engineering
- Stratified 80/20 train/test split
- Numerical scaling with `StandardScaler`
- Categorical encoding with `OneHotEncoder`
- Leakage-aware preprocessing
- Final dataset validation

### Engineered features

- `AgeGroup`
- `IncomeBand`
- `TenureGroup`
- `EarlyCareerFlag`
- `LongCommuteFlag`
- `YearsWithoutPromotion`
- `RoleTenureRatio`
- `ManagerTenureRatio`
- `CompanyExperienceRatio`
- `OvertimeRiskFlag`

### Week 2 output

- **1,470 rows retained**
- **0 missing values**
- **0 duplicate rows**
- **1,176 training records**
- **294 testing records**
- Training attrition rate: **16.16%**
- Testing attrition rate: **15.99%**
- **30 numerical features**
- **10 categorical features**
- **72 transformed machine-learning features**
- Final ML-ready dataset: **1,470 x 74**

The encoder and scaler are fitted on the **training set only** to reduce data leakage.

---

## Week 3 - Advanced Data Analysis, Statistical Validation & Feature Engineering

Week 3 builds directly on the Week 2 cleaned dataset (`cleaned_employee_attrition.csv`) - no re-cleaning of the raw data was performed.

### Analysis performed

- 14 advanced visualisations (numerical, categorical, bivariate, multivariate, correlation, group comparisons, target-variable analysis)
- 5 statistical hypothesis tests, each with stated H0/H1, method justification, test statistic, p-value, and business interpretation:
  - Chi-square test - Attrition x OverTime
  - Chi-square test - Attrition x Marital Status
  - Mann-Whitney U test - Monthly Income by Attrition
  - Mann-Whitney U test - Distance From Home by Attrition
  - Kruskal-Wallis test - Job Satisfaction across Job Role
  - Spearman correlation - Years at Company vs. Years with Current Manager
- Feature evaluation and selection (correlation analysis, mutual information, multicollinearity check)
- Dataset refinement into a final modelling dataset
- Business Insights and Recommendations report

### New engineered features

- `SatisfactionIndex` - composite mean of the four satisfaction/balance survey scores
- `CompaRatio` - Monthly Income relative to the average for the employee's job level
- `JobHopIntensity` - number of prior companies relative to total working years
- `StagnationRiskFlag` - compound flag for overtime + poor work-life balance + no recent promotion

### Feature evaluation decisions

- **Removed:** `LongCommuteFlag` - a deterministic re-encoding of `DistanceFromHome`, redundant.
- **Retained with a multicollinearity note:** `YearsAtCompany`, `YearsInCurrentRole`, `YearsWithCurrManager` (correlated 0.71-0.84), flagged for later modelling choices.
- **Retained with a data-quality note:** `PerformanceRating` has only two observed values across the dataset - a real limitation, not an error.

### Week 3 output

- Final modelling dataset: **1,470 rows x 45 columns**
- Business Insights and Recommendations report (Word document)

Key findings: overtime, marital status, and monthly income (relative to job-level peers) are all statistically significantly associated with attrition. Job satisfaction does **not** differ significantly across job roles - role-level attrition differences are better explained by workload and pay structure than by reported satisfaction.

---

## Project 1 Repository Structure

```text
data/
  WA_Fn-UseC_-HR-Employee-Attrition.csv
  cleaned_employee_attrition.csv
  employee_attrition_ml_ready.csv
  employee_attrition_final_modelling_dataset.csv

employee_attrition_analysis.ipynb
week2_feature_engineering_preprocessing_final.ipynb
week2_data_audit.csv
week2_preprocessing_summary.csv
week3_advanced_analysis_statistical_validation.ipynb
week3_business_insights_and_recommendations.docx
week3_data_dictionary.md
requirements.txt
```

## Tools Used (Project 1)

- Python
- Jupyter Notebook / Google Colab
- pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- scikit-learn

## Project 1 Status

### Completed

- Week 1: Business Understanding & EDA
- Week 2: Feature Engineering & Data Preprocessing
- Week 3: Advanced Data Analysis, Statistical Validation & Feature Engineering

This project is not being extended further - it stands as a complete three-week body of work, kept in this repository as part of the internship learning journey. Active development has moved to the HealthConnect Experience Lab below.

---

# Project 2: HealthConnect Experience Lab

## AnalystLab Africa Experience Lab - Data Science Track

Starting Week 4, all AnalystLab Africa interns began contributing to a single shared business problem - **HealthConnect Clinic**, a fictional healthcare provider - from their own professional track's perspective (Project Management, Data Analytics, Data Science, Machine Learning Engineering, Generative AI).

**Central project question:** How can HealthConnect Clinic use data and AI to reduce missed appointments and improve the patient support experience?

This part of the repository contains the **Data Science track's** contribution only.

### Project stages

Problem Understanding (Week 4) -> Analysis & Solution Design -> Development -> Testing & Refinement -> Final Presentation

---

## Week 4 - HealthConnect Project Kickoff & Problem Understanding

Week 4 is a planning and scoping stage - not a full analysis or a trained model. The goal was to understand the business problem, assess the real appointment dataset, and define the machine learning problem the Data Science track will pursue in later weeks.

### Dataset reviewed

`HealthConnect_Appointment_Data.csv` - 5,000 fictional, anonymised appointment records, 18 columns covering patient demographics, appointment details, booking information, prior no-show history, reminder information, distance to clinic, waiting time, and appointment outcome.

`HealthConnect_Data_Dictionary.xlsx` was not available at the time of this submission; column meanings were inferred from the data itself and flagged for confirmation once accessible.

### Key data findings

- No duplicate rows; missingness is low (under 2% on distance and waiting-time fields), and one apparent gap (`reminder_channel`) turned out to be structural, not a quality issue.
- The outcome variable is three-valued: `No-Show` (48.5%), `Attended` (46.3%), `Cancelled` (5.3%).
- `previous_no_shows` and `booking_lead_days` both show strong, consistent relationships with no-show rate.
- 5,000 appointments belong to only 1,696 unique patients (repeat patients), which affects how the data should be split for modelling.

### Proposed target variable

Binary: `did_not_attend` (`1` = No-Show, `0` = Attended). `Cancelled` appointments are excluded from this target, since a cancellation is a proactive, advance-notice action, operationally different from a silent no-show.

### Proposed approach

- Candidate features: prior no-show history, prior appointment count, booking lead time, distance to clinic, age, gender, appointment type, day, and time.
- `waiting_time_minutes` excluded pending confirmation of its exact definition - a possible data-leakage risk if it reflects actual (rather than scheduled) waiting time.
- Candidate models: logistic regression (interpretable baseline) and a tree-based model (Random Forest / Gradient Boosting).
- Proposed patient-grouped train/test split (`GroupShuffleSplit` by `patient_id`) to avoid the same patient appearing in both sets.
- Primary evaluation metrics: precision, recall, and ROC-AUC.

### Week 4 output

- `week4_ml_problem_definition.ipynb` - Machine Learning Problem Definition notebook, executed against the real dataset.
- `week4_project_summary.docx` - concise Week 4 Project Summary.

### Proposed focus for Week 5

Obtain and incorporate the official data dictionary to confirm column definitions, then move into deeper exploratory analysis of the confirmed feature set, implement the patient-grouped train/test split, and build an initial baseline logistic regression model.

---

## HealthConnect Repository Structure

```text
healthconnect-experience-lab/
  data/
    HealthConnect_Appointment_Data.csv
  week4_ml_problem_definition.ipynb
  week4_project_summary.docx
```

## Tools Used (HealthConnect - Data Science track)

- Python
- Jupyter Notebook / Google Colab
- pandas
- NumPy
- scikit-learn

## HealthConnect Project Status

### Completed

- Week 4: Problem Understanding (Data Science track)

### Next Stage

**Week 5: Analysis and Solution Design**

---

## Repository

https://github.com/Justcorplabs/employee-attrition-analysis


