# Employee Attrition Analysis
<<<<<<< HEAD

## Week 1 Data Science Internship Project

This project analyses the **IBM HR Analytics – Employee Attrition & Performance** dataset to identify patterns associated with employee turnover and translate them into practical business insights.

## Project Objective

The analysis focuses on:

* overall attrition levels;
* departments and job roles with higher attrition;
* overtime and business-travel patterns;
* differences in age, income, tenure, satisfaction, and work-life balance;
* statistical significance of observed differences;
* interaction effects such as **Overtime × Job Role** and **Business Travel × Department**.

## Dataset
=======

## Data Science Internship Project

This repository contains a multi-week employee attrition project based on the **IBM HR Analytics – Employee Attrition & Performance** dataset.

The project progresses from exploratory analysis in Week 1 to feature engineering and machine-learning preprocessing in Week 2.

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

## Week 1 — Business Understanding & Exploratory Data Analysis

Week 1 focused on understanding employee attrition patterns and translating them into business insights.

### Analysis included

- Data quality assessment
- Exploratory Data Analysis (EDA)
- Descriptive statistics
- Employee segmentation
- Correlation analysis
- Chi-square tests
- Welch's t-tests
- Overtime × Job Role interaction analysis
- Business Travel × Department interaction analysis
- Data visualisation
- Business recommendations

### Key findings

- Overall attrition was **16.12%**.
- Employees working overtime had substantially higher observed attrition.
- Frequent business travellers experienced higher attrition.
- Attrition varied across job roles and departments.
- Employees who left were generally younger, earned less, and had shorter organisational tenure.

These findings describe associations and do not establish causation.

---

## Week 2 — Feature Engineering & Data Preprocessing

Week 2 prepares the same dataset for machine-learning model development.
>>>>>>> 0a3bd40 (Add Week 2 feature engineering and preprocessing)

### Preprocessing performed

<<<<<<< HEAD
* **1,470 employees**
* **35 original variables**
* **237 employees who left**
* **1,233 employees who remained**
* Overall attrition rate: **16.12%**
* No missing values
* No duplicate rows

## Analysis Performed

The Jupyter Notebook includes:

* Business understanding
* Data quality assessment
* Data preparation
* Exploratory Data Analysis (EDA)
* Descriptive statistics
* Employee segmentation
* Correlation analysis
* Chi-square tests for categorical variables
* Welch's t-tests for numerical variables
* Overtime × Job Role interaction analysis
* Business Travel × Department interaction analysis
* Data visualisation
* Business recommendations
* Limitations and ethical considerations

## Key Findings

* Overall attrition was **16.12%**.
* Employees working overtime had substantially higher observed attrition.
* Frequent business travellers experienced higher attrition.
* Attrition varied across job roles and departments.
* Employees who left were generally younger, earned less, and had shorter organisational tenure.
* Interaction analysis showed that overtime and travel-related attrition patterns differed across roles and departments.


## Business Recommendations

The analysis suggests that organisations should:

* review persistent overtime and workload allocation;
* investigate high-attrition roles;
* support employees with frequent business travel;
* strengthen onboarding and early-career development;
* review compensation and career progression;
* monitor attrition trends across employee segments.

## Tools Used

* Python
* Jupyter Notebook
* pandas
* NumPy
* Matplotlib
* SciPy
=======
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
- Final ML-ready dataset: **1,470 × 74**

The encoder and scaler are fitted on the **training set only** to reduce data leakage.

---

## Repository Structure

```text
employee-attrition-analysis/
│
├── data/
│   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   ├── cleaned_employee_attrition.csv
│   └── employee_attrition_ml_ready.csv
│
├── employee_attrition_analysis.ipynb
├── week2_feature_engineering_preprocessing_final.ipynb
├── week2_data_audit.csv
├── week2_preprocessing_summary.csv
├── README.md
└── requirements.txt
```

---

## Tools Used

- Python
- Jupyter Notebook / Google Colab
- pandas
- NumPy
- Matplotlib
- SciPy
- scikit-learn

---

## Current Project Status

### Completed

- Week 1: Business Understanding & EDA
- Week 2: Feature Engineering & Data Preprocessing

### Next Stage

**Week 3: Machine Learning Model Development**

The ML-ready dataset will be used to train and compare classification models using metrics appropriate for an imbalanced target.

---

## Repository

https://github.com/Justcorplabs/employee-attrition-analysis

## Author

**Tinovimbanashe Shayamano**
>>>>>>> 0a3bd40 (Add Week 2 feature engineering and preprocessing)
