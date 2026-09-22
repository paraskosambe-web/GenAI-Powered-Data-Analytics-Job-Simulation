import pandas as pd
import numpy as np

# ==========================================
# 1. LOAD DATASET & BASIC INSPECTION
# ==========================================
file_path = 'Delinquency_prediction_dataset.xlsx'
df = pd.read_excel("C:\\Users\\Paras\\Downloads\\TATA\\data\\Delinquency_prediction_dataset.xlsx")

print("--- Dataset Shape ---")
print(df.shape)  # Output: (500, 19)

print("\n--- Column List & Data Types ---")
print(df.info())

print("\n--- Missing Values Count ---")
print(df.isnull().sum())

print("\n--- Summary Statistics (Numerical Features) ---")
print(df.describe())


# ==========================================
# 2. CATEGORICAL & TARGET VARIABLE ANALYSIS
# ==========================================
print("\n--- Target Variable Distribution (Delinquent_Account) ---")
print(df['Delinquent_Account'].value_counts(normalize=True))

print("\n--- Raw Employment Status Distribution ---")
print(df['Employment_Status'].value_counts())

print("\n--- Credit Card Type Breakdown ---")
print(df['Credit_Card_Type'].value_counts())

print("\n--- Location Distribution ---")
print(df['Location'].value_counts())

print("\n--- Check Duplicate Customer IDs ---")
print("Duplicates:", df['Customer_ID'].duplicated().sum())


# ==========================================
# 3. DATA CLEANING & FEATURE ENGINEERING
# ==========================================
# Clean text formatting inconsistencies in Employment_Status
df['Employment_Status_Clean'] = df['Employment_Status'].str.strip().str.capitalize()
df['Employment_Status_Clean'] = df['Employment_Status_Clean'].replace({'Emp': 'Employed'})

print("\n--- Cleaned Employment Status ---")
print(df['Employment_Status_Clean'].value_counts())

# Calculate total missed payments across Month_1 to Month_6
month_cols = ['Month_1', 'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6']
df['Calculated_Missed_6M'] = (df[month_cols] == 'Missed').sum(axis=1)

# Check for outliers in Credit Utilization (> 1.0 / 100%)
over_limit = df[df['Credit_Utilization'] > 1.0][['Customer_ID', 'Credit_Utilization', 'Delinquent_Account']]
print("\n--- Accounts with Credit Utilization > 100% ---")
print(over_limit)


# ==========================================
# 4. STATISTICAL IMPUTATION VALUES
# ==========================================
income_median = df['Income'].median()
credit_score_median = df['Credit_Score'].median()
loan_balance_median = df['Loan_Balance'].median()

print(f"\n--- Median Imputation Values ---")
print(f"Income Median: ${income_median:,.2f}")
print(f"Credit Score Median: {credit_score_median}")
print(f"Loan Balance Median: ${loan_balance_median:,.2f}")


# ==========================================
# 5. CORRELATION ANALYSIS
# ==========================================
numeric_df = df.select_dtypes(include=[np.number])
correlations = numeric_df.corr()['Delinquent_Account'].sort_values(ascending=False)

print("\n--- Numeric Feature Correlations with Delinquent_Account ---")
print(correlations)