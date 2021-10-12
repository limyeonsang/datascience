# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 09:56:49 2021

@author: 82109
"""
# %%
import pandas as pd
import numpy as np

data = pd.DataFrame({'Name':['a','b','c','d','e'],
                    'age':[10,20,30,np.NaN,50],})
print(data)

# %%
# interpolate
data.interpolate(inplace=True)
print(data)

# %%
# apply
def add(x):
    return x+1

print(data['age'].apply(add))

# %%
# filter
print(data.filter(regex="[g]")) 

# %%
# combine
combine_vertical = pd.concat([data, data])
print(combine_vertical)

combine_horizontal = pd.concat([data,data], axis=1)
print(combine_horizontal)

# %%
# output to excel
data.to_excel('data_excel.xlsx', index=False)

# output to text
data.to_csv('data_text.txt', sep='\t', index=False)

# output to pickle
data.to_pickle('data_pickle.pkl')

# %%
# read to excel
as_excel = pd.read_excel('data_excel.xlsx')

# read to text
as_text = pd.read_csv('data_text.txt', delimiter='\t')

# read to pickle
as_pickle = pd.read_pickle('data_pickle.pkl')
print(as_pickle)