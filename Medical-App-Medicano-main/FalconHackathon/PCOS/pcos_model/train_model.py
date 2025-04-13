import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Load the dataset
data_path = os.path.join(os.path.dirname(__file__), 'pcos_dataset.csv')
data = pd.read_csv(data_path, sep=',')  # Use comma as separator

print("📄 Raw data preview:")
print(data.head())
print("📄 Columns before cleaning:", data.columns.tolist())

# Clean column names
data.columns = data.columns.str.strip().str.replace(r'\s+', ' ', regex=True)

# Rename inconsistent column names to match code expectations
column_renames = {
    'I beta-HCG(mIU/mL)': 'I beta-HCG(mIU/mL)',
    'II beta-HCG(mIU/mL)': 'II beta-HCG(mIU/mL)'
}

# Automatically rename columns
for col in data.columns:
    if 'I ' in col and 'beta-HCG' in col:
        column_renames[col] = 'I beta-HCG(mIU/mL)'
    if 'II' in col and 'beta-HCG' in col:
        column_renames[col] = 'II beta-HCG(mIU/mL)'

data.rename(columns=column_renames, inplace=True)

# Drop unnecessary columns
cols_to_drop = ['Sl. No', 'Patient File No.']
data.drop(columns=[col for col in cols_to_drop if col in data.columns], inplace=True)

print("📄 Cleaned columns:", data.columns.tolist())

# Adjusted selected features to match available columns
selected_features = [
    'I beta-HCG(mIU/mL)', 'II beta-HCG(mIU/mL)', 'AMH(ng/mL)'
]

# Validate features
missing = [feat for feat in selected_features if feat not in data.columns]
if missing:
    raise ValueError(f"❌ Missing columns in dataset: {missing}")

# Convert columns to numeric and handle invalid values
for col in selected_features:
    data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert invalid entries to NaN

# Handle NaN values (either fill or drop)
data[selected_features] = data[selected_features].fillna(data[selected_features].median())  # Or use dropna()

# Prepare data
X = data[selected_features]
y = data['PCOS (Y/N)']  # Ensure this matches the exact column name

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model and scaler
model_dir = os.path.dirname(__file__)
joblib.dump(model, os.path.join(model_dir, 'pcos_model.pkl'))
joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))

print("✅ Model and scaler saved successfully.")
print("✅ Trained on features:", selected_features)
