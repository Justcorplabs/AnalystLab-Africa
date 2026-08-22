# Data Dictionary — Employee Attrition Final Modelling Dataset (Week 3)

**File:** `employee_attrition_final_modelling_dataset.csv`
**Rows:** 1,470 | **Columns:** 45
**Source:** IBM HR Analytics Employee Attrition & Performance dataset, cleaned in Week 2, refined in Week 3.

## Original source fields (Weeks 1–2)

| Column | Type | Description |
|---|---|---|
| Age | int | Employee age in years |
| Attrition | str | Target variable — `Yes`/`No`, whether the employee left the company |
| BusinessTravel | str | Frequency of business travel |
| DailyRate | int | Daily pay rate |
| Department | str | Department the employee belongs to |
| DistanceFromHome | int | Distance from home to workplace (miles) |
| Education | int | Education level, 1 (Below College) – 5 (Doctor) |
| EducationField | str | Field of education |
| EnvironmentSatisfaction | int | Satisfaction with work environment, 1–4 |
| Gender | str | Employee gender |
| HourlyRate | int | Hourly pay rate |
| JobInvolvement | int | Job involvement rating, 1–4 |
| JobLevel | int | Job level within the organisation, 1–5 |
| JobRole | str | Specific job role |
| JobSatisfaction | int | Satisfaction with the job, 1–4 |
| MaritalStatus | str | Marital status |
| MonthlyIncome | int | Monthly income |
| MonthlyRate | int | Monthly pay rate |
| NumCompaniesWorked | int | Number of companies worked at prior to this one |
| OverTime | str | Whether the employee regularly works overtime |
| PercentSalaryHike | int | Percentage salary increase at last review |
| PerformanceRating | int | Performance rating, 3 (Excellent) or 4 (Outstanding) — see limitation note |
| RelationshipSatisfaction | int | Satisfaction with workplace relationships, 1–4 |
| StockOptionLevel | int | Stock option level, 0–3 |
| TotalWorkingYears | int | Total years of professional experience |
| TrainingTimesLastYear | int | Number of trainings attended last year |
| WorkLifeBalance | int | Work-life balance rating, 1–4 |
| YearsAtCompany | int | Tenure at the current company |
| YearsInCurrentRole | int | Years in current role |
| YearsSinceLastPromotion | int | Years since last promotion |
| YearsWithCurrManager | int | Years with current manager |

## Week 2 engineered fields

| Column | Type | Description |
|---|---|---|
| AttritionFlag | int | Binary encoding of Attrition (1 = Yes, 0 = No) |
| AgeGroup | str | Age bucketed into 5 bands (18-25 … 56+) |
| IncomeBand | str | MonthlyIncome bucketed into quartiles (Low … High) |
| TenureGroup | str | YearsAtCompany bucketed into 5 bands |
| EarlyCareerFlag | int | 1 if TotalWorkingYears ≤ 5 |
| YearsWithoutPromotion | int | YearsAtCompany − YearsSinceLastPromotion (clipped at 0) |
| RoleTenureRatio | float | YearsInCurrentRole ÷ YearsAtCompany |
| ManagerTenureRatio | float | YearsWithCurrManager ÷ YearsAtCompany |
| CompanyExperienceRatio | float | YearsAtCompany ÷ TotalWorkingYears |
| OvertimeRiskFlag | int | 1 if OverTime = Yes |

*Note: `LongCommuteFlag` (Week 2) was removed in Week 3 — see Feature Evaluation decision below.*

## Week 3 engineered fields (new)

| Column | Type | Description | Business rationale |
|---|---|---|---|
| SatisfactionIndex | float | Mean of EnvironmentSatisfaction, JobSatisfaction, RelationshipSatisfaction, WorkLifeBalance | Single composite sentiment score |
| CompaRatio | float | MonthlyIncome ÷ mean MonthlyIncome for that employee's JobLevel | Pay competitiveness within level, decoupled from seniority |
| JobHopIntensity | float | NumCompaniesWorked ÷ (TotalWorkingYears + 1) | Career mobility rate, independent of career length |
| StagnationRiskFlag | int | 1 if OverTime=Yes AND WorkLifeBalance ≤ 2 AND YearsSinceLastPromotion ≥ 4 | Flags a compound "burned out and stalled" risk segment |

## Feature evaluation decisions (Week 3, Part 5)

- **Removed:** `LongCommuteFlag` — a deterministic threshold re-encoding of `DistanceFromHome` (r ≈ 0.88 by construction); redundant.
- **Retained with a multicollinearity note:** `YearsAtCompany`, `YearsInCurrentRole`, `YearsWithCurrManager` (Spearman ρ up to 0.84) — flagged for Week 4 modelling choices (e.g. tree-based models are largely insensitive to this).
- **Retained with a data-quality note:** `PerformanceRating` has only two observed values (3, 4) across the whole dataset and near-zero mutual information with the target — a real limitation of the source data, not an error.
- **Retained despite low mutual information:** `StagnationRiskFlag` — mutual information near 0 due to its rarity (~1.8% of employees), but the raw group attrition-rate gap (29.6% vs 15.9%) is business-meaningful and domain-justified.
