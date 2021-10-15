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
print(data.filter(regex="[g]")) 

