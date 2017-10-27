import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C': [1,2,3]}

df = pd.DataFrame(d)

print(df)

#dropping missing value in row
print(df.dropna())

#dropping missing value in col
print(df.dropna(axis=1))

#using thresold to dropping data
print(df.dropna(thresh=2))

#filling non na value using fillna
print(df.fillna('Ashish'))

print(df['A'].fillna(df['A'].mean()))
