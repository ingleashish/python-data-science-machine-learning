import numpy as np
import pandas as pd

d = {'Company':['Google', 'Google', 'Microsoft', 'Microsoft', 'Facebook', 'Facebook'], 'Persons':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl','Sarah'],'Sales':[200, 220, 400, 344, 650, 123]}

df = pd.DataFrame(d)

print(df)

byComp = df.groupby('Company')

print(byComp.mean())

print(byComp.sum())

print(byComp.std())#standard deviation

print(byComp.count())

print(byComp.max())

print(byComp.min())


print(byComp.describe())

print(byComp.describe().transpose())
