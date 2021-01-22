#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:27:42 2020

@author: andrewczeropski
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

#Read data from csv file
data = pd.read_csv("/Users/andrewczeropski/Desktop/Fun Python Stuff/Stock Analyzer/OXY.csv")

#Select target
y = data['Close']

#Select predictors
col_to_use = ['Open', 'High', 'Low', 'Volume']
X = data[col_to_use]

#Set up training and testing variables and run split
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

#Create model using XGBRegressor
my_model = XGBRegressor(n_estimators = 500, learning_rate = 0.05, n_jobs = 4)
my_model.fit(X_train, y_train,
             early_stopping_rounds = 10,
             eval_set = [(X_valid, y_valid)],
             verbose = False)

#Make predictions and return MAE
predictions = my_model.predict(X_valid)
print('Mean Absolute Error: ' + str(mean_absolute_error(predictions, y_valid)))

high_value_row = data[data.High == data.High.max()]
low_value_row = data[data.Low == data.Low.min()]

print('The highest stock price was: $', float(high_value_row['High']))
print('The lowest stock price was: $', float(low_value_row['Low']))
