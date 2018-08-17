# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:57:51 2018

@author: muralish
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Featured_data.csv')
x_train = data[data['source']=='Train']
y_train = x_train['SalePrice']
x_train = x_train.drop('source',axis=1)
x_train = x_train.drop('SalePrice',axis=1)

x_test = data[data['source']=='Test']
x_test = x_test.drop('source',axis=1)
x_test = x_test.drop('SalePrice',axis=1)

from sklearn.preprocessing import RobustScaler
robustscaler = RobustScaler()
x_train = robustscaler.fit_transform(x_train)
x_test = robustscaler.fit_transform(x_test)

#Random Forest Classifier
from sklearn.ensemble  import RandomForestClassifier
RFC = RandomForestClassifier()
RFC.fit(x_train,y_train)
y_test = RFC.predict(x_train)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred = y_test, y_true = y_train)

y_pred = RFC.predict(x_test)
y_pred = [int(i) for i in y_pred]
y_pred = y_pred.values


testID = data[data['source']=='Test']
testID = testID.Index
output = pd.dataFrame(index = x_test.)

retest = pd.read_csv('first_submission.csv')


#Upgrade

from sklearn.metrics import mean_squared_error
y_pred_train = RFC.predict(x_train)
mean_squared_error(y_train, y_pred_train)

plt.scatter(y_pred_train,y_train,alpha=0.75,color='b')
plt.xlabel('pred')
plt.ylabel('Actual')
