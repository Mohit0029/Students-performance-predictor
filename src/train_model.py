import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

print("--- Starting Model Training Script ---")

# --- 1. Load Data ---
# Create paths relative to the script's location
# This makes the script runnable from anywhere
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'student_performance_data.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'models')

df = pd.read_csv(DATA_PATH)
print("Data loaded successfully.")

# --- 2. Data Cleaning & Pre-processing ---
df.drop_duplicates(inplace=True)

# Convert categorical columns to numerical using one-hot encoding
df_model = pd.get_dummies(df, columns=['Gender', 'City', 'State', 'Board', 'ParentalEducation', 'ParentalOccupation', 'Medium', 'HasTuition'], drop_first=True)
print("Data pre-processing complete.")

# --- 3. Feature Selection ---
# Define features (X) and target (y)
X = df_model.drop(columns=['StudentID', 'FirstName', 'LastName', 'FinalScore', 'MathScore', 'ScienceScore', 'EnglishScore'])
y = df_model['FinalScore']

# --- 4. Train the Model ---
print("Training the Random Forest model...")
# We use the full dataset here to train the final model for deployment
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)
print("Model training complete.")

# --- 5. Save the Model and Columns ---
# This is crucial for our web app to work correctly
os.makedirs(MODEL_DIR, exist_ok=True) # Ensure the 'models' directory exists
joblib.dump(rf_model, os.path.join(MODEL_DIR, 'random_forest_model.joblib'))

# Save the column names used for training
model_columns = list(X.columns)
joblib.dump(model_columns, os.path.join(MODEL_DIR, 'model_columns.joblib'))

print(f"Model and columns saved successfully in the '{MODEL_DIR}' folder.")
print("--- Script Finished ---")
