import numpy as np

numbers = np.arange(1, 6)

numbers2 = numbers.copy()

numbers[1] *= 10

print(numbers, numbers2)

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
g = grades.copy()
print(grades)
print(grades.reshape(1, 12))
print(grades)

print(grades.resize(1, 12))
print(grades)
print(g)
print(g.flatten())

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
ravel = grades.ravel()
# ravel[0] = 100
grades = np.array([[100, 96, 70], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])
print(np.hstack((grades, grades2)))
print(np.vstack((grades, grades2)))
