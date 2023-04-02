from pprint import pprint
import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
pprint(s1)
s2 = pd.to_numeric(s1, errors='coerce')
s2=s2[s2.notnull()]
pprint(s2)