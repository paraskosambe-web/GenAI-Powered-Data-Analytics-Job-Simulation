import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

# =========================================================
# 1. LOAD DATASET & DATA CLEANING
# =========================================================
file_path = 'Delinquency_prediction_dataset.xlsx'
df = pd.read_excel("C:\\Users\\Paras\\Downloads\\TATA\\data\\Delinquency_prediction_dataset.xlsx")

# Clean text formatting in Employment_Status
df['Employment_Status'] = df['Employment_Status'].str.strip().str.capitalize()
df['Employment_Status'] = df['Employment_Status'].replace({'Emp': 'Employed'})

# =========================================================
# 2. FEATURE ENGINEERING (Task 2 Behavioral Features)
# =========================================================
# Calculate cumulative missed and late payment counts across Month 1 to Month 6
month_cols = ['Month_1', 'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6']
df['Recent_Missed_Count'] = (df[month_cols] == 'Missed').sum(axis=1)
df['Recent_Late_Count'] = (df[month_cols] == 'Late').sum(axis=1)

# Separate Features (X) and Target (y)
X = df.drop(columns=['Customer_ID', 'Delinquent_Account'])
y = df['Delinquent_Account']

# Categorize columns by data type
num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = X.select_dtypes(include=['object']).columns.tolist()

# =========================================================
# 3. PREPROCESSING PIPELINE & TRANSFORMATION
# =========================================================
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, num_cols),
        ('cat', cat_transformer, cat_cols)
    ]
)

# Train-Test Split (80/20 Stratified Split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================================================
# 4. PREDICTIVE MODEL PIPELINE (Decision Tree & Logistic Regression)
# =========================================================
# Model Option 1: Cost-Sensitive Decision Tree
dt_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier(max_depth=5, random_state=42, class_weight='balanced'))
])

dt_pipeline.fit(X_train, y_train)
y_pred_dt = dt_pipeline.predict(X_test)
y_proba_dt = dt_pipeline.predict_proba(X_test)[:, 1]

# Model Option 2: Logistic Regression (Benchmark)
lr_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(class_weight='balanced', random_state=42))
])

lr_pipeline.fit(X_train, y_train)
y_pred_lr = lr_pipeline.predict(X_test)
y_proba_lr = lr_pipeline.predict_proba(X_test)[:, 1]

print("--- Decision Tree AUC-ROC Score ---", roc_auc_score(y_test, y_proba_dt))
print("--- Logistic Regression AUC-ROC Score ---", roc_auc_score(y_test, y_proba_lr))