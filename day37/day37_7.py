import pandas as pd
from pprint import pprint

ser = pd.Series(range(6), index=[
                'white', 'white', 'blue', 'green', 'green', 'yellow'])
print(ser)

print(ser.white)