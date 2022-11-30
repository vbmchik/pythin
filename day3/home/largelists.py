from random import randint
from datetime import datetime

#print(set([1,2,3])^set([4,2,5]))
print("start ", datetime.now())
# [1,2,3]^[3,4,5] = [1,2,4,5]
# [1,2,3]&[3,4,5] = [3]
list1 = [randint(1, 100000) for x in range(1, 1000001)]
list2 = [randint(1, 100000) for x in range(1, 1000001)]
print("lists created ", datetime.now())
print(len((set(list1)^set(list2))))
print("diff calculated", datetime.now())

