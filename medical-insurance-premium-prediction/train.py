import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics


insurance_dataset=pd.read_csv('insurance_dataset.csv')

import warnings
warnings.filterwarnings("ignore")

'''
# first 5 rows of the dataframe
print(insurance_dataset.head())

# number of rows and columns
print(insurance_dataset.shape)

# getting some informations about the dataset
print(insurance_dataset.info())

# checking for missing values
print(insurance_dataset.isnull().sum())

# statistical Measures of the dataset
print(insurance_dataset.describe())

# distribution of age value
sns.set()
plt.figure(figsize=(6,6))
sns.displot(insurance_dataset['age'])
plt.title('Age Distribution')
#print(plt.show())

# Gender column
plt.figure(figsize=(9,9))
sns.countplot(x='gender', data=insurance_dataset)
plt.title('Sex Distribution')
#print(plt.show())

insurance_dataset['gender'].value_counts()

# bmi distribution
plt.figure(figsize=(6,6))
sns.displot(insurance_dataset['bmi'])
plt.title('BMI Distribution')
#print(plt.show())

# children column
plt.figure(figsize=(6,6))
sns.countplot(x='children', data=insurance_dataset)
plt.title('Children')
#print(plt.show())

insurance_dataset['children'].value_counts()

# smoker column
plt.figure(figsize=(6,6))
sns.countplot(data=insurance_dataset , x='smoker')
plt.title('smoker')
#print(plt.show())

insurance_dataset['smoker'].value_counts()
insurance_dataset['region'].value_counts()
'''

# encoding sex column
insurance_dataset.replace({'gender':{'male':0,'female':1}}, inplace=True)

# encoding 'smoker' column
insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

# encoding 'region' column
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

# encoding 'medical_history' column
insurance_dataset.replace({'medical_history':{'Diabetes':0,'High blood pressure':1,'Heart disease':2,'None':3}}, inplace=True)

# encoding 'family_medical_history' column
insurance_dataset.replace({'family_medical_history':{'Diabetes':0,'High blood pressure':1,'Heart disease':2,'None':3}}, inplace=True)

# encoding 'exercise_frequency' column
insurance_dataset.replace({'exercise_frequency':{'Never':0,'Occasionally':1,'Rarely':2,'Frequently':3}}, inplace=True)

# encoding 'occupation' column
#insurance_dataset.replace({'occupation':{'Blue collar':0,'White collar':1,'Student':2,'Unemployed':3}}, inplace=True)


# Assuming df is your DataFrame with the target variable in the last column
X = insurance_dataset.iloc[:, :-1]  # Features (all columns except the last one)
Y = insurance_dataset.iloc[:, -1]   # Target variable (last column)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
#print(X.shape, X_train.shape, X_test.shape)


'''from sklearn.impute import SimpleImputer
# Use SimpleImputer to fill in missing values in your feature matrix
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)  # Use the same imputer for consistency'''

from sklearn.ensemble import HistGradientBoostingRegressor
# Use RandomForestRegressor with the imputed data
regressor = HistGradientBoostingRegressor()
regressor.fit(X_train, Y_train)

# prediction on training data
training_data_prediction = regressor.predict(X_train)

# R squared value on training set
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared value on training set: ', r2_train)

# prediction on test data
test_data_prediction = regressor.predict(X_test)

# R squared value on test set
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R squared value on test set: ', r2_test)

accuracy_test = regressor.score(X_test, Y_test)
print(accuracy_test)

import pickle
pickle.dump(regressor, open('train.pkl','wb'))
#depickling
regressor = pickle.load(open('train.pkl','rb'))