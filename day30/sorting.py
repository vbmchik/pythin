import datetime
from functools import reduce
from random import randint
from itertools import combinations
  
print(datetime.datetime.now())
t = [ x for x in range(1,90_000_000) ]
print(datetime.datetime.now())
t.sort(reverse=True)
print(t[0])
print(datetime.datetime.now())

t = [x for x in range(1, 9000)]
print(datetime.datetime.now())
for i in range(0,len(t)-1):
    for j in range(i+1, len(t)):
        if t[i] < t[j]:
            a = t[i]
            t[i] = t[j]
            t[j] = a
print(t[0])
print(datetime.datetime.now())



