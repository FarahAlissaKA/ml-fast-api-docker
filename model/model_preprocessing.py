import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae

import warnings
warnings.filterwarnings('ignore') # Suppress warnings for cleaner output

# Load datasets: calories data and exercise data
df1 = pd.read_csv('calories.csv')
df2 = pd.read_csv('exercise.csv')

# Merge the two datasets on a common column
df = pd.merge(df1, df2, how='outer')

# Drop unnecessary columns: Weight and Duration
to_remove = ['Weight', 'Duration']
df.drop(to_remove, axis=1, inplace=True)

# Convert categorical gender values ('male', 'female') to numerical values (0, 1)
df.replace({'male': 0, 'female': 1}, inplace=True)

# Define features (input) and target (output)
features = df.drop(['User_ID', 'Calories'], axis=1)
target = df['Calories'].values

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Normalize the feature data using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the RandomForestRegressor model
model = RandomForestRegressor()

# Train the model on the training data
model.fit(X_train, y_train)

# Save the trained model to a file using joblib for later use in the API
joblib.dump(model, '../backend/model.joblib')

# Evaluate the model on training data
train_preds = model.predict(X_train)
print('Training Error: ', mae(y_train, train_preds))

# Evaluate the model on test data    
test_preds = model.predict(X_test)
print('Validation Error: ', mae(y_test, test_preds))