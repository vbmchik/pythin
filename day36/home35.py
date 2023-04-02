from pprint import pprint
import numpy
import random

def random_array():
    l = [random.randint(1,100) for _ in range(3) ]
    return l

def numgenerator(n):
    for _ in range(n):
        yield numpy.array([random_array(), random_array(), random_array()])

g = numgenerator(3)

pprint(next(g))
pprint(next(g))
pprint(next(g))


