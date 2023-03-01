import numpy as np

numbers = np.arange(1,6)

print(numbers*2)
print(numbers**3)
print(numbers+10)


numbers2 = np.linspace(1.1, 3.3, 5)
print(numbers)
print(numbers2)
print(numbers*numbers2)


numbers+=10
print(numbers>=13)
numbers2 = np.linspace(1.1,5.5,5)
print(numbers)
print(numbers2)
print(numbers2<numbers)
print(numbers2+2>numbers-10)