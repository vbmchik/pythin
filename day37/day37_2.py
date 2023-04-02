from pprint import pprint
import pandas as pd
import numpy as np

s = pd.Series([-12, 3, 4, 23], index=['a', 'b', 'c', 'd'])
pprint(s)
pprint(s.values)
pprint(s.index)

print(s['b':'d'])
print(s[2])

s[2] = 12
s['c'] = 14
pprint(s[s > 0])
pprint(s/2)
pprint(np.log(s))

ser = pd.Series([1, 2, 3, 4, 1, 2, 6, 7, 5, 4, 2, 1, 3])
pprint(ser.unique())
pprint(ser.value_counts())
s2 = np.log(s)
pprint(s2[s2>2])
pprint(s2[s2.isnull()])
pprint(s2[s2.notnull()])
pprint(ser[ser%2==0])