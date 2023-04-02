import pandas as pd
from pprint import pprint
colors=['red','yellow', 'orange', 'blue', 'green']
mydict = {"red":2000, 'blue': 1000, 'yellow': 500, 'orange':1000}
pprint(mydict)
ms = pd.Series(mydict, index=colors)
pprint(ms)
mydict2 = {"red":300, 'yellow': 1000, 'black':700}
ms2=pd.Series(mydict2)
pprint(ms+ms2)