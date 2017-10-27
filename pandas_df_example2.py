import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101) #to get same random number

df = pd.DataFrame(randn(5,4),['A','B', 'C','D','E'],['W','X','Y','Z'])
print(df)

#conditional selection

print(df > 0)

print(df[df > 0])

print(df['W']>0)

print(df[df['W']>0])

print(df[df['W']>0]['X'])

print(df[df['W']>0][['X','Y']])

#multiple condition on df
print(df[(df['W'] > 0) & (df['Y'] < 1)]) #python and to &

print(df[(df['W'] > 0) & (df['Y'] > 1)])

print(df[(df['W'] > 0) | (df['Y'] > 1)]) #python or to |

#set and reset index
print(df.reset_index())

newindex = 'MH UP KA GA TL'.split()

df['STATES'] = newindex

print(df)

print(df.set_index('STATES'))
