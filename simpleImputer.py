# %%
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# %%
df = pd.DataFrame({'col1':[np.nan, 2, 3], 'col2':[4, np.nan, 6]}) #, 'target':[10, np.nan, 9]})

df

# %%,
transformer = SimpleImputer(missing_values=np.nan, strategy='mean')
transformer.fit(df)
df = transformer.transform(df)
print(df)

"""
missing_values: int, float, str, np.nan or None, default=np.nan
The placeholder for the missing values. All occurrences of missing_values will be imputed. 

strategy: default='mean'
-If “mean”, then replace missing values using the mean along each column. Can only be used with numeric data.
-If “median”, then replace missing values using the median along each column. Can only be used with numeric data.
-If “most_frequent”, then replace missing using the most frequent value along each column. Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.
-If “constant”, then replace missing values with fill_value. Can be used with strings or numeric data.
"""

# %%
transformer.fit_transform(df)
# %%
