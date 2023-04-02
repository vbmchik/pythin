import pandas as pd
import numpy as np
from pprint import pprint

frame = pd.DataFrame(np.arange(16).reshape(4,4),index = ['red', 'blue', 'white', 'green'], columns=['ball', 'pen', 'pencil', 'paper'])
pprint(frame)
pprint(frame.index)
pprint(frame.columns)
pprint(frame.values)
pprint(frame['paper'])
pprint(frame.paper)
pprint(frame.loc['blue'])
pprint(frame.loc[['blue','red']])
frame.index.name = 'color'
frame.columns.name = 'items'

frame["bubble"] = [12,4,126,7]
pprint(frame)
del frame["bubble"]
pprint(frame.isin([1.0,2.0]))
pprint(frame[frame%2==0])

# 1 2       1 3
# 3 4       2 4

pprint(frame.T)
pprint(frame.idxmax())
pprint(frame.idxmin())