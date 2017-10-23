#install pandas distrubution using conda install pandas or pip install pandas

import numpy as np
import pandas as pd
## SERIES ##
print("#### SERIES ####")

labels = ['a','b','c']
my_data = [10,20,30]
np_arr = np.array(my_data)
d = {'a' : 10, 'b': 20, 'c' : 30}

print("lables as char list : {} mydata as number list: {} numpy array from mydata list: {} and dictionary: {}".format(labels, my_data, np_arr, d))

pd_series = pd.Series(data=my_data)
print(pd_series)

pd_series = pd.Series(data=my_data, index=labels)
print(pd_series)
