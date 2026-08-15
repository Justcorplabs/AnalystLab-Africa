"""
Employee Attrition Analysis
Week 1 Data Science Internship Project

Workflow:
Business Understanding -> Data Understanding -> Data Cleaning -> EDA ->
Statistics -> Visualisation -> SQL -> Interaction Analysis ->
Optional Machine Learning -> Dashboard Outputs -> Business Insights

Author: Tinovimbanashe Shayamano
"""

from pathlib import Path
import sqlite3
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
DASHBOARD_DIR = BASE_DIR / "dashboard_data"

OUTPUT_DIR.mkdir(exist_ok=True)
DASHBOARD_DIR.mkdir(exist_ok=True)

# 1. BUSINESS UNDERSTANDING
business_questions = [
    "What is the overall employee attrition rate?",
    "Which departments and job roles have the highest attrition rates?",
    "Is overtime associated with attrition?",
    "Is frequent business travel associated with higher attrition?",
    "How do age, income, tenure, satisfaction and work-life balance differ by attrition?",
    "Which employee segments should HR investigate first?"
]

# 2. DATA UNDERSTANDING
df = pd.read_csv(DATA_PATH)

print("=" * 80)
print("EMPLOYEE ATTRITION ANALYSIS")
print("=" * 80)
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

# 3. DATA CLEANING AND VALIDATION
missing_values = int(df.isna().sum().sum())
duplicates = int(df.duplicated().sum())

constant_columns = [
    column for column in df.columns
    if df[column].nunique(dropna=False) == 1
]
identifier_columns = ["EmployeeNumber"]

analysis_df = df.drop(columns=constant_columns + identifier_columns).copy()
analysis_df["AttritionFlag"] = (analysis_df["Attrition"] == "Yes").astype(int)

quality_summary = pd.DataFrame({
    "Metric": [
        "Rows", "Original Columns", "Missing Values",
        "Duplicate Rows", "Constant Columns Removed",
        "Identifier Columns Removed"
    ],
    "Value": [
        len(df), df.shape[1], missing_values, duplicates,
        len(constant_columns), len(identifier_columns)
    ]
})
quality_summary.to_csv(OUTPUT_DIR / "data_quality_summary.csv", index=False)

# IQR outlier screening
outlier_rows = []
for col in analysis_df.select_dtypes(include=np.number).columns:
    q1 = analysis_df[col].quantile(0.25)
    q3 = analysis_df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    count = ((analysis_df[col] < lower) | (analysis_df[col] > upper)).sum()
    outlier_rows.append({
        "Column": col,
        "Outlier_Count": int(count),
        "Outlier_Percentage": round(count / len(analysis_df) * 100, 2)
    })

pd.DataFrame(outlier_rows).sort_values(
    "Outlier_Percentage", ascending=False
).to_csv(OUTPUT_DIR / "outlier_summary.csv", index=False)

# 4. EDA
attrition_summary = (
    analysis_df["Attrition"]
    .value_counts()
    .rename_axis("Attrition")
    .reset_index(name="Employees")
)
attrition_summary["Percentage"] = (
    attrition_summary["Employees"] / len(analysis_df) * 100
).round(2)
attrition_summary.to_csv(DASHBOARD_DIR / "overall_attrition.csv", index=False)

def attrition_by_category(data, column, minimum_group_size=1):
    result = (
        data.groupby(column, observed=False)
        .agg(
            Employees=("AttritionFlag", "size"),
            Attrition_Count=("AttritionFlag", "sum"),
            Attrition_Rate=("AttritionFlag", "mean")
        )
        .reset_index()
    )
    result["Attrition_Rate"] = (result["Attrition_Rate"] * 100).round(2)
    return (
        result[result["Employees"] >= minimum_group_size]
        .sort_values("Attrition_Rate", ascending=False)
        .reset_index(drop=True)
    )

for column, filename in [
    ("Department", "attrition_by_department.csv"),
    ("JobRole", "attrition_by_job_role.csv"),
    ("OverTime", "attrition_by_overtime.csv"),
    ("BusinessTravel", "attrition_by_business_travel.csv"),
    ("MaritalStatus", "attrition_by_marital_status.csv")
]:
    attrition_by_category(analysis_df, column).to_csv(
        DASHBOARD_DIR / filename, index=False
    )

# Age and tenure segmentation
analysis_df["AgeBand"] = pd.cut(
    analysis_df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)
analysis_df["TenureBand"] = pd.cut(
    analysis_df["YearsAtCompany"],
    bins=[-1, 1, 3, 5, 10, np.inf],
    labels=["0-1 years", "2-3 years", "4-5 years", "6-10 years", "11+ years"]
)

attrition_by_category(analysis_df, "AgeBand").to_csv(
    DASHBOARD_DIR / "attrition_by_age_band.csv", index=False
)
attrition_by_category(analysis_df, "TenureBand").to_csv(
    DASHBOARD_DIR / "attrition_by_tenure_band.csv", index=False
)

# 5. DESCRIPTIVE STATISTICS
selected_numeric = [
    "Age", "MonthlyIncome", "DistanceFromHome",
    "TotalWorkingYears", "YearsAtCompany",
    "YearsInCurrentRole", "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]
descriptive = analysis_df.groupby("Attrition")[selected_numeric].agg(
    ["mean", "median", "std"]
)
descriptive.to_csv(OUTPUT_DIR / "descriptive_statistics_by_attrition.csv")

# 6. INFERENTIAL STATISTICS
categorical_columns = [
    "OverTime", "BusinessTravel", "Department", "JobRole",
    "MaritalStatus", "JobSatisfaction", "EnvironmentSatisfaction",
    "WorkLifeBalance", "JobInvolvement"
]

chi_rows = []
for col in categorical_columns:
    table = pd.crosstab(analysis_df[col], analysis_df["Attrition"])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    chi_rows.append({
        "Variable": col,
        "Chi_square": round(chi2, 4),
        "Degrees_of_Freedom": dof,
        "p_value": p,
        "Significant_at_0.05": p < 0.05
    })

chi_results = pd.DataFrame(chi_rows).sort_values("p_value")
chi_results.to_csv(OUTPUT_DIR / "chi_square_tests.csv", index=False)

left_group = analysis_df[analysis_df["Attrition"] == "Yes"]
stay_group = analysis_df[analysis_df["Attrition"] == "No"]

t_rows = []
for col in selected_numeric:
    t_stat, p = stats.ttest_ind(
        left_group[col], stay_group[col],
        equal_var=False, nan_policy="omit"
    )
    t_rows.append({
        "Variable": col,
        "Mean_Left": round(left_group[col].mean(), 2),
        "Mean_Stayed": round(stay_group[col].mean(), 2),
        "t_statistic": round(t_stat, 4),
        "p_value": p,
        "Significant_at_0.05": p < 0.05
    })

t_results = pd.DataFrame(t_rows).sort_values("p_value")
t_results.to_csv(OUTPUT_DIR / "welch_t_tests.csv", index=False)

# 7. VISUALISATIONS
plt.figure(figsize=(6, 4))
analysis_df["Attrition"].value_counts().plot(kind="bar", rot=0)
plt.title("Employee Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Employees")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "attrition_count.png", dpi=150)
plt.close()

for column in ["OverTime", "BusinessTravel", "Department", "JobRole"]:
    table = attrition_by_category(analysis_df, column)
    plt.figure(figsize=(8, 5))
    table.sort_values("Attrition_Rate").set_index(column)["Attrition_Rate"].plot(
        kind="barh"
    )
    plt.title(f"Attrition Rate by {column}")
    plt.xlabel("Attrition Rate (%)")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / f"attrition_rate_by_{column.lower()}.png",
        dpi=150
    )
    plt.close()

# 8. SQL ANALYSIS
conn = sqlite3.connect(":memory:")
df.to_sql("employees", conn, index=False, if_exists="replace")

sql_queries = {
    "department": """
        SELECT Department,
               COUNT(*) AS Employees,
               SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
               ROUND(
                   100.0 * SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) / COUNT(*),
                   2
               ) AS Attrition_Rate
        FROM employees
        GROUP BY Department
        ORDER BY Attrition_Rate DESC;
    """,
    "job_role": """
        SELECT JobRole,
               COUNT(*) AS Employees,
               SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
               ROUND(
                   100.0 * SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) / COUNT(*),
                   2
               ) AS Attrition_Rate
        FROM employees
        GROUP BY JobRole
        ORDER BY Attrition_Rate DESC;
    """,
    "overtime": """
        SELECT OverTime,
               COUNT(*) AS Employees,
               SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
               ROUND(
                   100.0 * SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) / COUNT(*),
                   2
               ) AS Attrition_Rate
        FROM employees
        GROUP BY OverTime
        ORDER BY Attrition_Rate DESC;
    """
}

for name, query in sql_queries.items():
    pd.read_sql_query(query, conn).to_csv(
        OUTPUT_DIR / f"sql_{name}.csv", index=False
    )

conn.close()

# 9. INTERACTION ANALYSIS
overtime_role = (
    analysis_df.groupby(["JobRole", "OverTime"], observed=False)
    .agg(
        Employees=("AttritionFlag", "size"),
        Attrition_Count=("AttritionFlag", "sum"),
        Attrition_Rate=("AttritionFlag", "mean")
    )
    .reset_index()
)
overtime_role["Attrition_Rate"] = (
    overtime_role["Attrition_Rate"] * 100
).round(2)
overtime_role.to_csv(
    OUTPUT_DIR / "interaction_overtime_by_job_role.csv", index=False
)

travel_department = (
    analysis_df.groupby(["Department", "BusinessTravel"], observed=False)
    .agg(
        Employees=("AttritionFlag", "size"),
        Attrition_Count=("AttritionFlag", "sum"),
        Attrition_Rate=("AttritionFlag", "mean")
    )
    .reset_index()
)
travel_department["Attrition_Rate"] = (
    travel_department["Attrition_Rate"] * 100
).round(2)
travel_department.to_csv(
    OUTPUT_DIR / "interaction_travel_by_department.csv", index=False
)

# 10. OPTIONAL MACHINE LEARNING
try:
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import (
        accuracy_score, precision_score, recall_score,
        f1_score, roc_auc_score
    )

    ml_df = df.drop(columns=constant_columns + identifier_columns).copy()
    X = ml_df.drop(columns="Attrition")
    y = (ml_df["Attrition"] == "Yes").astype(int)

    num_features = X.select_dtypes(include=np.number).columns.tolist()
    cat_features = X.select_dtypes(exclude=np.number).columns.tolist()

    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=1000, class_weight="balanced", random_state=42
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, class_weight="balanced", random_state=42
        )
    }

    model_rows = []

    for name, estimator in models.items():
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("model", estimator)
        ])
        pipe.fit(X_train, y_train)
        pred = pipe.predict(X_test)
        prob = pipe.predict_proba(X_test)[:, 1]

        model_rows.append({
            "Model": name,
            "Accuracy": accuracy_score(y_test, pred),
            "Precision": precision_score(y_test, pred, zero_division=0),
            "Recall": recall_score(y_test, pred, zero_division=0),
            "F1": f1_score(y_test, pred, zero_division=0),
            "ROC_AUC": roc_auc_score(y_test, prob)
        })

    pd.DataFrame(model_rows).to_csv(
        OUTPUT_DIR / "model_comparison.csv", index=False
    )

except ImportError:
    print("scikit-learn is not installed; ML section skipped.")

# 11. BUSINESS INSIGHTS
overall_rate = (
    analysis_df["AttritionFlag"].mean() * 100
)

overtime_table = attrition_by_category(analysis_df, "OverTime")
travel_table = attrition_by_category(analysis_df, "BusinessTravel")
role_table = attrition_by_category(analysis_df, "JobRole")

insights = pd.DataFrame({
    "Insight": [
        "Overall attrition rate",
        "Highest overtime attrition group",
        "Highest business travel attrition group",
        "Highest job-role attrition group"
    ],
    "Result": [
        f"{overall_rate:.2f}%",
        f"{overtime_table.iloc[0]['OverTime']} ({overtime_table.iloc[0]['Attrition_Rate']:.2f}%)",
        f"{travel_table.iloc[0]['BusinessTravel']} ({travel_table.iloc[0]['Attrition_Rate']:.2f}%)",
        f"{role_table.iloc[0]['JobRole']} ({role_table.iloc[0]['Attrition_Rate']:.2f}%)"
    ]
})
insights.to_csv(OUTPUT_DIR / "key_business_insights.csv", index=False)

print("\nAnalysis complete.")
print(f"Outputs saved to: {OUTPUT_DIR}")
print(f"Dashboard files saved to: {DASHBOARD_DIR}")
