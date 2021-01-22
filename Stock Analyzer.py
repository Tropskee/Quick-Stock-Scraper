#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:05:24 2020

@author: andrewczeropski
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import mplfinance as mpf
import matplotlib.pyplot as plt


oxy = pd.read_csv("/Users/andrewczeropski/Desktop/Fun Python Stuff/Stock Analyzer/OXY.csv")

train_data = oxy[oxy.Date < '2019-04-04'].copy()
test_data = oxy[oxy.Date > '2019-04-04'].copy()

y = train_data['Close']
train_data.drop(['Close', 'Date', 'Adj Close'], axis = 1, inplace = True)

X = train_data
X_test = test_data

my_pipeline = Pipeline(steps = [
    ('model', RandomForestRegressor(n_estimators = 50,random_state = 0))
])

scores = -1 * cross_val_score(my_pipeline, X, y, 
                              cv = 5, 
                              scoring = 'neg_mean_absolute_error')
print(scores.mean())


#Graph data using candlestick plot
oxy.iloc[:,0] = pd.to_datetime(oxy.iloc[:,0], format = '%Y-%m-%d')
oxy = oxy.set_index(pd.DatetimeIndex(oxy['Date']))
print(oxy.head())

plt.figure(figsize = (20,10))
mpf.plot(oxy [-30:], type = 'candle', mav = 5, volume=True, show_nontrading = True)
