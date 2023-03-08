import datetime
from functools import reduce
from random import randint
from itertools import combinations
  
l = [[2, 8, 9, 3, 1, 11, 12],    # 1 - index 0 1
     [2, 4, 6, 3, 4, 1, 3, 4],   # 2 - index 1 1,2 
     [1, 3, 14, 15, 16, 17],     # 3 - index 2 1,2,3
     [1, 2, 3, 4],               # 4 - index 3 1,2,3,4
     [3, 4, 5],                  # 5 - index 4 1,2,3,4,5
     [1, 2, 3, 4, 5, 6, 7]]      # 6 - index 5 1,2,3,4,5,6



p = set(l[0])
for i in range (1, len(l)):
     p = set(l[i])&p
print(p)

# reduce!!!  [1,2,3,4,5,6]
t = [ x for x in range(1,90000000) ]
print(datetime.datetime.now())
r = reduce(lambda x, y: x + y, t)
print(datetime.datetime.now())


p = t[0]
for i in range (1, len(t)):
     p = p + t[i]
print(datetime.datetime.now())   
print(sum(t))
print(datetime.datetime.now())
print(p)
print(r)
print(reduce(lambda x,y: set(x)&set(y), l))