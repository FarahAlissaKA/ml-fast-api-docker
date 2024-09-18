import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae

import warnings
warnings.filterwarnings('ignore')

df1 = pd.read_csv('calories.csv')
df2 = pd.read_csv('exercise.csv')

df = pd.merge(df1, df2, how='outer')
#df.to_csv('../backend/calories_merged.csv', index=False, header=True)

to_remove = ['Weight', 'Duration']
df.drop(to_remove, axis=1, inplace=True)

df.replace({'male': 0, 'female': 1}, inplace=True)

features = df.drop(['User_ID', 'Calories'], axis=1)
target = df['Calories'].values

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestRegressor()

model.fit(X_train, y_train)

joblib.dump(model, '../backend/model.joblib')

train_preds = model.predict(X_train)
print('Training Error: ', mae(y_train, train_preds))
    
test_preds = model.predict(X_test)
print('Validation Error: ', mae(y_test, test_preds))