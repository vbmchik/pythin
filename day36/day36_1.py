from pprint import pprint
import numpy


a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8], float)
a[3] = '12.4'
a = a.reshape(4,2)
pprint(a)


a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]], float)
a[2][0] = '12.4'
pprint(a)


a = numpy.array([
    [[1, 2, 7], [4, 5, 9], [4, 5, 9]],
    [[6, 3, 8], [2, 3, 1], [4, 3, 3]],
    [[7, 8, 9], [9, 5, 6], [7, 4, 9]],
    [[1, 2, 7], [4, 5, 9], [4, 5, 9]],
    [[6, 3, 8], [2, 3, 1], [4, 3, 3]],
    [[7, 8, 9], [9, 5, 6], [7, 4, 9]]
], float)
a[2][1][1] = '12.4'
a = a.reshape(2,27)
a.fill(0)
pprint(a)
