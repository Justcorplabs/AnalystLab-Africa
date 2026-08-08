Employee Attrition Analysis

Week 1 Data Science Internship Project

This project explores the IBM HR Analytics – Employee Attrition & Performance dataset to understand employee attrition patterns and identify workforce factors associated with employees leaving the organisation.

The analysis focuses on business understanding, data quality, exploratory data analysis, statistical testing, employee segmentation, interaction analysis, and business recommendations.

Project Objective

The objective of this analysis is to understand employee attrition and answer key business questions such as:

What is the overall employee attrition rate?

Which departments and job roles experience higher attrition?

Is overtime associated with employee attrition?

Does frequent business travel relate to higher attrition?

How do age, income, tenure, job satisfaction, and work-life balance differ between employees who leave and those who remain?

Which employee groups may require greater attention from HR?

Are the observed differences statistically significant?

Do combinations such as overtime and job role reveal additional attrition patterns?

Dataset

Dataset: IBM HR Analytics – Employee Attrition & Performance

The dataset contains:

1,470 employee records

35 original variables

Target variable: Attrition

237 employees who left

1,233 employees who remained

Overall attrition rate: 16.12%

The dataset contains no missing values and no duplicate rows.

Analysis Workflow

The Jupyter Notebook covers the following areas:

1. Business Understanding

Defines the employee-retention problem and the business questions addressed by the analysis.

2. Data Understanding and Quality Assessment

Examines:

dataset dimensions;

data types;

missing values;

duplicate records;

unique values;

constant columns;

identifier fields.

3. Data Preparation

Columns that do not provide analytical value are excluded from the analytical dataset.

Examples include:

EmployeeCount

Over18

StandardHours

EmployeeNumber

A binary AttritionFlag is also created to support numerical analysis.

4. Descriptive Statistics

Summarises the numerical and categorical characteristics of the workforce.

5. Exploratory Data Analysis

Investigates attrition across:

departments;

job roles;

overtime status;

business travel;

marital status;

job satisfaction;

environment satisfaction;

job involvement;

work-life balance;

stock option level;

job level.

6. Numerical Comparisons

Compares employees who left with employees who remained using variables such as:

Age

Monthly Income

Distance From Home

Total Working Years

Years at Company

Years in Current Role

Years Since Last Promotion

Years With Current Manager

7. Employee Segmentation

Employees are grouped into business-friendly segments such as:

age bands;

company-tenure bands.

Attrition rates are then compared across these groups.

8. Correlation Exploration

Examines linear relationships between numerical variables and the binary attrition indicator.

Correlation is treated as an association and not evidence of causation.

9. Statistical Significance Testing

The notebook includes inferential statistical testing to determine whether observed differences are statistically significant.

Chi-Square Tests

Chi-square tests are applied to categorical variables including:

OverTime

BusinessTravel

Department

JobRole

MaritalStatus

JobSatisfaction

EnvironmentSatisfaction

WorkLifeBalance

JobInvolvement

A significance level of 0.05 is used.

Welch's Independent T-Tests

Welch's t-tests compare numerical variables between employees who left and employees who remained.

Variables tested include:

Age

MonthlyIncome

DistanceFromHome

TotalWorkingYears

YearsAtCompany

YearsInCurrentRole

YearsSinceLastPromotion

YearsWithCurrManager

Welch's test is used because it does not require the two groups to have equal variances.

10. Interaction Analysis

The notebook also investigates combinations of workforce characteristics.

Overtime × Job Role

Attrition rates are compared across job roles while separating employees by overtime status.

This analysis helps determine whether the relationship between overtime and attrition is concentrated in particular job roles.

Business Travel × Department

Business-travel categories are analysed within each department.

This helps determine whether travel-related attrition patterns differ across organisational areas.

11. Business Findings and Recommendations

The technical results are translated into practical HR insights and recommendations.

12. Limitations and Ethical Considerations

The analysis acknowledges that:

association does not establish causation;

the dataset is a static sample;

voluntary and involuntary attrition are not separated;

small groups may produce unstable rates;

sensitive employee characteristics should not be used for discriminatory employment decisions.

Key Findings

The exploratory analysis identified several notable patterns:

Overall employee attrition is approximately 16.12%.

Employees working overtime have substantially higher observed attrition than employees who do not work overtime.

Frequent business travellers experience higher observed attrition.

Attrition varies considerably across job roles.

Employees who leave are younger on average.

Employees who leave have lower average monthly income.

Employees who leave generally have shorter organisational and career tenure.

Distance from home is somewhat higher among employees who leave.

Interaction analysis provides additional insight into how overtime varies across job roles and how travel patterns vary across departments.

These findings describe relationships within the dataset and should not be interpreted as proof that any individual factor causes an employee to leave.

Business Recommendations

Based on the analysis, the organisation should consider:

Reviewing persistent overtime and workload allocation.

Investigating employee experience in roles with elevated attrition.

Evaluating support for employees with frequent business travel.

Strengthening onboarding, mentoring, and early-career development.

Reviewing compensation and career-progression structures.

Monitoring retention patterns across departments and employee segments.

Collecting richer exit and engagement data to support future analysis.

Tools and Technologies

Python

Jupyter Notebook

pandas

NumPy

Matplotlib

SciPy
