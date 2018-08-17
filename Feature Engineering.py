# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 08:17:00 2018

@author: muralish
"""

import pandas as pd
data = pd.read_csv('Cleaned.csv')
data['Alley']=data['Alley'].replace('Grv1','Grvl') # MAde a mistake in the previous module




data['GarageYrBlt']=2018-data['GarageYrBlt'].astype(int)
data['YearBuilt']=2018-data['YearBuilt'].astype(int)
data['YearRemodAdd']=2018-data['YearRemodAdd'].astype(int)
data['YrSold']=2018-data['YrSold'].astype(int)

x= data.drop('SalePrice',axis=1)
y=data['SalePrice']


data['BldgType'] = data['BldgType'].replace({'1Fam':'SingleFamilyDetached',
                                                             '2fmCon':'Two-family Conversion',
                                                             'TwnhsE' : 'Twnhs'
                                                             })


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le = LabelEncoder()

i='BldgType'
data1[i] = le.fit_transform(data1[i])
data1 = pd.get_dummies(data1, columns=[i])
data1= data1.drop('BldgType_3',axis=1)

i='BsmtCond'
data1[i] = le.fit_transform(data1[i])
data1 = pd.get_dummies(data1, columns=[i])
data1= data1.drop('BsmtCond_3',axis=1)

i='BsmtExposure'
data1[i] = le.fit_transform(data1[i])
data1 = pd.get_dummies(data1, columns=[i])
data1= data1.drop('BsmtExposure_3',axis=1)


i='BsmtFinType1'
data1[i] = le.fit_transform(data1[i])
data1 = pd.get_dummies(data1, columns=[i])
data1= data1.drop('BsmtFinType1_5',axis=1)

i='BsmtFinType2'
data1[i] = le.fit_transform(data1[i])
data1 = pd.get_dummies(data1, columns=[i])
data1= data1.drop('BsmtFinType2_5',axis=1)

var_mod = ['BsmtQual','CentralAir','Condition1','Condition2']
le = LabelEncoder()
for i in var_mod:
    data1[i] = le.fit_transform(data1[i])
    
data1 = pd.get_dummies(data1, columns=['BsmtQual','CentralAir','Condition1','Condition2'])
data1 = data1.drop('CentralAir_1',axis=1)
data1 = data1.drop('CentralAir_1',axis=1)
data1 = data1.drop('Condition2_7',axis=1)



var_mod = ['Foundation','Functional', 'GarageCond','GarageFinish', 'GarageQual', 'GarageType',
'Heating', 'HeatingQC', 'HouseStyle', 'KitchenQual', 'LandContour', 'LandSlope',
'LotConfig','LotShape','MSZoning', 'MasVnrType', 'MiscFeature', 'Neighborhood', 'PavedDrive',
 'RoofMatl', 'RoofStyle', 'SaleCondition','SaleType','Street','Utilities']
le = LabelEncoder()
for i in var_mod:
    data1[i] = le.fit_transform(data1[i])
    
data1 = pd.get_dummies(data1, columns=['Foundation','Functional', 'GarageCond','GarageFinish', 'GarageQual', 'GarageType',
'Heating', 'HeatingQC', 'HouseStyle', 'KitchenQual', 'LandContour', 'LandSlope',
'LotConfig','LotShape','MSZoning', 'MasVnrType', 'MiscFeature', 'Neighborhood', 'PavedDrive',
 'RoofMatl', 'RoofStyle', 'SaleCondition','SaleType','Street','Utilities'])
     
for count in var_mod:
     data1=data1.drop(count + '_0',axis=1)

data1= data1.drop('Id',axis=1)

submission = pd.DataFrame({ col: data1[col] for col in data1.columns})
submission.to_csv('Featured_data.csv', index=False)