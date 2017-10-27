import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
print(hier_index)

hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df = pd.DataFrame(np.random.randn(6,2), hier_index,['A', 'B'])
print(df)

#indexing multilevel
print(df.loc['G1'])
print(df.loc['G1'].loc[1])

#printing unnamed index
print(df.index.names)

df.index.names = ['Groups', 'Num']
print(df.index.names)
print(df)

#grabbing value from df using multi level
print(df.loc['G1'].loc[2]['B'])

#grabbing using cross index on multi level index

print(df.xs('G1'))
print(df.xs(1, level='Num'))
