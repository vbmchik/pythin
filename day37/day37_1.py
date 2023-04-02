from pprint import pprint
import pandas as pd
import numpy as np

df = pd.DataFrame({'X': [23, 12, 34, 32, 34], 'Y': [
                  54, 23, 54, 23, 54], 'Z': [88, 44, 33, 22, 56]})
pprint(df)

s = pd.Series([2, 3, 4, 5, 6])
pprint(s)

df.index = pd.date_range('2023/4/1', periods=df.shape[0])
pprint(df)
