from functools import reduce
def redo(x,y):
    return x*y

l = [1,2,3,4,5]
r = reduce(redo, l)
print(r)
# [1+2]  = 3 . [1*2]  = 2
# [3+3]  = 6 . [2*3]  = 6
# [6+4]  = 10  [6*4]  = 24
# [10+5] = 15  [24*5] = 120