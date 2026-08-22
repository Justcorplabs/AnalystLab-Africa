# Employee Attrition Analysis

## Data Science Internship Project

This repository contains a multi-week employee attrition project based on the **IBM HR Analytics - Employee Attrition & Performance** dataset.

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
- **Retained with a multicollinearity note:** `YearsAtCompany`, `YearsInCurrentRole`, `YearsWithCurrManager` (correlated 0.71-0.84), flagged for Week 4 modelling choices.
- **Retained with a data-quality note:** `PerformanceRating` has only two observed values across the dataset - a real limitation, not an error.

### Week 3 output

- Final modelling dataset: **1,470 rows x 45 columns**
- Business Insights and Recommendations report (Word document)

Key findings: overtime, marital status, and monthly income (relative to job-level peers) are all statistically significantly associated with attrition. Job satisfaction does **not** differ significantly across job roles - role-level attrition differences are better explained by workload and pay structure than by reported satisfaction.

---

## Repository Structure

```text
employee-attrition-analysis/
|
|-- data/
|   |-- WA_Fn-UseC_-HR-Employee-Attrition.csv
|   |-- cleaned_employee_attrition.csv
|   |-- employee_attrition_ml_ready.csv
|   `-- employee_attrition_final_modelling_dataset.csv
|
|-- employee_attrition_analysis.ipynb
|-- week2_feature_engineering_preprocessing_final.ipynb
|-- week2_data_audit.csv
|-- week2_preprocessing_summary.csv
|-- week3_advanced_analysis_statistical_validation.ipynb
|-- week3_business_insights_and_recommendations.docx
|-- week3_data_dictionary.md
|-- README.md
`-- requirements.txt
```

---

## Tools Used

- Python
- Jupyter Notebook / Google Colab
- pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- scikit-learn

---

## Current Project Status

### Completed

- Week 1: Business Understanding & EDA
- Week 2: Feature Engineering & Data Preprocessing
- Week 3: Advanced Data Analysis, Statistical Validation & Feature Engineering

### Next Stage

**Week 4: Machine Learning Model Development, Evaluation & Business Recommendations**

The Week 3 final modelling dataset will be used to train and compare classification models using metrics appropriate for an imbalanced target (recall, precision, ROC-AUC rather than accuracy alone).

---

## Repository

https://github.com/Justcorplabs/employee-attrition-analysis

## Author

**Bynadge Joseph Jakarasi **
