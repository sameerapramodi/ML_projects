# -*- coding: utf-8 -*-
"""first-project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uDzSPFlNkYnI6_Nzei185A5zgvHVOUBh

if the target variable is solubility, the model could predict how soluble a new compound is likely to be based on its descriptors.

# Load data
"""

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/delaney_solubility_with_descriptors.csv')
df

"""MolLogP,	MolWt,	NumRotatableBonds,	AromaticProportion are X variables.
when we build a ML model to predict the Y variable or the log S is equal to the function of all the X variables here. or we use these four variables to predict the log S variable.

# Data Preparation

## data seperation
"""

y = df ['logS']
y

x = df.drop('logS', axis = 1)
x

"""## Data spliting as Training and Testing data"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

x_train

x_test

"""# Modle Building

## Linear Regression

Training the model
"""

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)

"""Applyimg the model to make the prediction"""

y_lr_train_pred = lr.predict(x_train)
y_test_pred = lr.predict(x_test)

print(y_lr_train_pred)

print(y_test_pred)

"""# Evaluate Model Performance

compare the predicted value and actual value
"""

y_train

y_lr_train_pred

from sklearn.metrics import mean_squared_error, r2_score

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_test_pred)
lr_test_r2 = r2_score(y_test, y_test_pred)

print ('LR MSE (Train): ', lr_train_mse)
print ('LR R2 (Train): ', lr_train_r2)
print ('LR MSE (Test): ', lr_test_mse)
print ('LR R2 (Test): ', lr_test_r2)

lr_results = pd.DataFrame(['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
# Changed 'Dataframe' to 'DataFrame' to use the correct pandas DataFrame constructor
lr_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
lr_results

lr_train_mse

"""## Random forest"""

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(x_train, y_train)

"""Applying the model to make predictions"""

y_rf_train_pred = rf.predict(x_train)
y_rf_test_pred = rf.predict(x_test)

from sklearn.metrics import mean_squared_error, r2_score

rf_train_mse = mean_squared_error(y_train, y_lr_train_pred)
rf_train_r2 = r2_score(y_train, y_lr_train_pred)

rf_test_mse = mean_squared_error(y_test, y_test_pred)
rf_test_r2 = r2_score(y_test, y_test_pred)

rf_results = pd.DataFrame(['Random Forest', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
# Changed 'Dataframe' to 'DataFrame' to use the correct pandas DataFrame constructor
rf_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
rf_results

df_models = pd.concat([lr_results, rf_results], axis=0).reset_index()
df_models

import matplotlib.pyplot as plt

# Assuming y_lr_train_pred contains the linear regression predictions on training data
plt.scatter(x=y_train, y=y_lr_train_pred, alpha=0.3)  # Changed y=y_lr_train to y=y_lr_train_pred
plt.plot()

import matplotlib.pyplot as plt # Imports the matplotlib library
import numpy as np

plt.figure(figsize=(5,5)) # Changed 'pit' to 'plt' to call the figure function from the matplotlib library
plt.scatter(x=y_train, y=y_lr_train_pred, alpha=0.3)

z = np.polyfit(y_train, y_lr_train_pred, 1)
p = np.poly1d(z)

plt.plot(y_train, p(y_train), '#F8766D')
plt.ylabel('Predict LogS')
plt.xlabel('Experimental LogS')

# Assuming y_lr_train_pred contains the linear regression predictions on training data