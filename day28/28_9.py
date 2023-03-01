import numpy as np

numbers = np.arange(1,6)

numbers2 = numbers.view()
numbers[1] *= 10
numbers2[2] *= 5
print(numbers, numbers2)
print(id(numbers), id(numbers2))
del numbers2
del numbers
numbers = np.arange(1, 6)
numbers2 = numbers[1:3]
numbers[2] *= 10
numbers[4] *=2
print(numbers, numbers2)

