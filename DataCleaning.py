# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 02:32:21 2018

@author: muralish
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 02:23:08 2018

@author: muralish
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Import, Merge datasets
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
train['source']='Train'
test['source']='Test'
data=pd.concat([train,test],ignore_index=True)
    
#Find NILL values and clean them
null_values = data.apply(lambda x: sum(x.isnull()))
     #Filling Alley with the mode
data['Alley'].unique()
data['Alley'].mode()     #Grv1
data[['Alley']]=data[['Alley']].fillna('Grv1')
     #Filling basement condition with the mode
data['BsmtCond'].unique()
data['BsmtCond'].mode()     #TA
data[['BsmtCond']]=data[['BsmtCond']].fillna('TA')
     #Filling basement exposure with the mode
data['BsmtExposure'].unique()
data['BsmtExposure'].mode()     #No
data[['BsmtExposure']]=data[['BsmtExposure']].fillna('No')
     #Drop null values from BsmtFinType1,BsmtFinType2
data = data.dropna(subset=['BsmtFinSF1'])
     #Replace missing values in BsmtFinType1: Rating of basement finished area
data['BsmtFinType1'].unique()
data['BsmtFinType1'].mode()     #Unf
data[['BsmtFinType1']]=data[['BsmtFinType1']].fillna('Unf')
     #Replace missing values in BsmtFinType2: Rating of basement finished area (if multiple types)
data['BsmtFinType2'].unique()
data['BsmtFinType2'].mode()     #Unf
data[['BsmtFinType2']]=data[['BsmtFinType2']].fillna('Unf')
     #Drop null values from BsmtFullbath, BsmtHalfbath

     #Replace missing values in BsmtQual: Evaluates the height of the basement
data['BsmtQual'].unique()
data['BsmtQual'].mode()  #TA
data[['BsmtQual']]=data[['BsmtQual']].fillna('TA')
     #Remove PoolQC



data.Exterior1st.mode()
data[['Exterior1st']]=data[['Exterior1st']].fillna('VinylSd')
data.Exterior2nd.mode()
data[['Exterior2nd']]=data[['Exterior2nd']].fillna('VinylSd')
data.Functional.mode()
data[['Functional']]=data[['Functional']].fillna('Typ')
round(data.GarageArea.mean())
data[['GarageArea']]=data[['GarageArea']].fillna(473)
data.GarageCars.mode()
data[['GarageCars']]=data[['GarageCars']].fillna(2)
data.KitchenQual.mode()
data[['KitchenQual']]=data[['KitchenQual']].fillna('TA')
data.MSZoning.mode()
data[['MSZoning']]=data[['MSZoning']].fillna('RL')
data.SaleType.mode()
data[['SaleType']]=data[['SaleType']].fillna('WD')
data.Utilities.mode()
data[['Utilities']]=data[['Utilities']].fillna('AllPub')
data.BsmtFullBath.mode()
data[['BsmtFullBath']]=data[['BsmtFullBath']].fillna(0)
data = data.drop('PoolQC',axis=1)

data.BsmtFinSF2.mode()
data[['BsmtFinSF2']]=data[['BsmtFinSF2']].fillna(0)


data.BsmtHalfBath.mode()
data[['BsmtHalfBath']]=data[['BsmtHalfBath']].fillna(0)

data.TotalBsmtSF.mean()
data[['TotalBsmtSF']]=data[['TotalBsmtSF']].fillna(1052)


from scipy.stats import mode
     #Clean fence data
fence_mode = data.pivot_table(values='Fence',
                                   columns='ExterQual',
                                   aggfunc=lambda x: x.mode().iat[0])
miss_bool = data['Fence'].isnull() 
data.loc[miss_bool,'Fence'] = data.loc[miss_bool,'ExterQual'].apply(lambda x: fence_mode[x])


     #Electrical Mode
data.Electrical.mode()
data[['Electrical']]=data[['Electrical']].fillna('SBrkr')


     #Clean fireplace quality data
fire_place_qu = data.pivot_table(values='FireplaceQu',
                                   columns='Alley',
                                   aggfunc=lambda x: x.mode().iat[0])
data[['FireplaceQu']]=data[['FireplaceQu']].fillna('Gd')


     #Garage
data[['GarageCond']]=data[['GarageCond']].fillna('TA')
data[['GarageFinish']]=data[['GarageCond']].fillna('TA')
     #GarageFinish
Garage_Finish = data.pivot_table(values='GarageFinish',
                                   columns='GarageCond',
                                   aggfunc=lambda x: x.mode().iat[0])
miss_bool = data['GarageFinish'].isnull() 
data.loc[miss_bool,'GarageFinish'] = data.loc[miss_bool,'GarageCond'].apply(lambda x: Garage_Finish[x])

     #Garage Quality
data[['GarageQual']]=data[['GarageQual']].fillna('TA')
     #GarageType
garage_type = data.pivot_table(values='GarageType',
                                   columns='GarageCond',
                                   aggfunc=lambda x: x.mode().iat[0])
miss_bool = data['GarageType'].isnull() 
data.loc[miss_bool,'GarageType'] = data.loc[miss_bool,'GarageCond'].apply(lambda x: garage_type[x])

     #Garage Year built
year_comp = data[['GarageYrBlt','YearBuilt']]
miss_bool = data['GarageYrBlt'].isnull() 
data.loc[miss_bool,'GarageYrBlt'] = data.loc[miss_bool,'YearBuilt']

     #MasVnrType
vnr_type = data.pivot_table(values='MasVnrType',
                                   columns='MSZoning',
                                   aggfunc=lambda x: x.mode().iat[0])

data[['MasVnrType']]=data[['MasVnrType']].fillna('None')

#Misc Feature
misc_feature = data.pivot_table(values='MiscFeature',
                                   columns='MasVnrType',
                                   aggfunc=lambda x: x.mode().iat[0])
miss_bool = data['MiscFeature'].isnull() 
data.loc[miss_bool,'MiscFeature'] = data.loc[miss_bool,'MasVnrType'].apply(lambda x: misc_feature[x])


     #LotFrontage
Lot_Frontage = round(data.pivot_table(values= 'LotFrontage', columns = 'LotConfig'))
miss_bool = data['LotFrontage'].isnull()
data.loc[miss_bool,'LotFrontage'] = data.loc[miss_bool,'LotConfig'].apply(lambda x: Lot_Frontage[x])


     #MasVnrArea
Mas_Vnr_Area  = round(data.pivot_table(values='MasVnrArea',
                                   columns='MasVnrType',
                                  ))
miss_bool = data['MasVnrArea'].isnull()
data.loc[miss_bool,'MasVnrArea'] = data.loc[miss_bool,'MasVnrType'].apply(lambda x: Mas_Vnr_Area[x])



submission = pd.DataFrame({ x: data[x] for x in data.columns})
submission.to_csv('Cleaned.csv', index=False)
