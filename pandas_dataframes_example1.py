import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101) #to get same random number

df = pd.DataFrame(randn(5,4),['A','B', 'C','D','E'],['W','X','Y','Z'])
print(df)

print(df['W']) #Indexing DataFrame

print(type(df['W']))# type of Series

print(df.W) #avoid this but it work

print(df[['W', 'Z']])# get Sub DataFrame

df['NEW'] = df['W'] + df['Z'] #creating new col in DataFrame using arithmetic operation

print(df)

#removing col from DataFrame

df_drop_copy = df.drop('NEW',axis=1)#it remove from and made copy but wont change on original DataFrame axis=1 is important

print(df)
print(df_drop_copy)
df.drop('NEW',axis=1, inplace=True)#permanently remove from DataFrame

print(df)

#to remove row use axis=0 which is default and for col axis=1
print(df.drop('E'))

print(df)

print(df.shape)#return tuple which is row,col value

#SELECTING ROWS
print(df.loc['A'])#retrun row series
print(df.iloc[2])

print(df.loc['B','Y'])
print(df.loc[['A','B'],['W','X']])
