import math
from pprint import pprint
import numpy

a = numpy.array([1, 2, 3], float)
b = numpy.array([3, 4, 5], float)
pprint(a+b)
pprint(a-b)
pprint(a*b)
pprint(b/a)
pprint(a % b)
pprint(b**a)
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[6, 7, 8], [4, 5, 8]])
pprint(a+b)
pprint(a-b)
pprint(a*b)
pprint(b/a)
pprint(a % b)
pprint(b**a)
pprint(numpy.sqrt(a))

for x in a:
    pprint(x)

for d,f,g in a:
    print(d)
    print(g)
    print(f)


l = a<b
t = numpy.logical_and(a>0,a<3)
p = numpy.logical_not(l)
pprint(l)
pprint(p)
pprint(t)
pprint(numpy.where(a>3,1,0))