from pprint import pprint
import pandas as pd
data = {
    "color":['blue', 'green', 'yellow', 'red', 'white'],
    "object":['ball', 'pen', 'pencil', 'paper', 'mug'],
    'price':[1.2,1.0,0.7,0.9,1.8]
}
frame = pd.DataFrame(data)
pprint(frame)
frame1 = pd.DataFrame(data,columns=['object', 'price'])
pprint(frame1)