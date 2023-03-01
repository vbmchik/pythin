import random
import numpy as np
from datetime import datetime as dt

print(dt.now())  
rolls_list = [random.randrange(1,7) for i in range(0, 6_000_000)]
print(dt.now())
rolls_list_2 = np.random.randint(1,7,6_000_000)
print(dt.now())
print(len(rolls_list_2))
