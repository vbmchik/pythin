#Реализуйте генератор колоды карт(52)

import random


def coloda():
    nums = [2,3,4,5,6,7,8,9,10,'prince','queen', 'king', 'ace']
    kinds = ['пики', 'крести', 'бубы', 'червы']
    for x in kinds:
        for y in nums:
            yield (x,y)

l = list(coloda())
rlist = []
for x in range(len(l)-1, -1, -1):
    k = random.randint(0,x)
    rlist.append(l.pop(k))
    
print(rlist)

