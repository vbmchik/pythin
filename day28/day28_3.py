import numpy as np

numbers = np.zeros(10)
numbers = np.ones((2,4), dtype=int)
numbers=np.full((4,5),13)

numbers = np.arange(5)
numbers = np.arange(5,10)
numbers = np.arange(10,1, -2)

numbers = np.linspace(0.0, 1.0, num=5)
numbers = np.arange(1,21).reshape(4,5)

numbers = np.arange(1,100001).reshape(4,25000)
print(numbers)