from pprint import pprint
import numpy

a = numpy.array([1, 2, 3], float)
pprint(a)
a = a[:, numpy.newaxis]
pprint(a)
a = a[:, numpy.newaxis]
pprint(a)


a = numpy.arange(5, dtype=float)
pprint(a)
a = numpy.ones((2,3), dtype=float)
pprint(a)
a = numpy.zeros(5, dtype=int)
pprint(a)
