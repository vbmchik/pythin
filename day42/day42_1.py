# Первая задача

# У вас есть массив чисел. 
# Напишите три функции, которые вычисляют сумму этих чисел: 
# с for -циклом, с while -циклом, с рекурсией.

from random import randint

def badsum(index, l):
    if index == 0:
        return l[0]
    else:
        return l[index]+badsum(index-1,l)
    
def bettersum(l):
    if len(l) == 0:
        return 0
    else:
        return l.pop() + bettersum(l)
    
# f(12) -> 12 + f(11) -> 12 + 11 + f(10) -> 12 + 11 + 10 + f(9)   
# f(l) -> pop() + f(l)    
n = 12
l = [randint(1,20) for _ in range(n)]

s = 0
for x in l:
    s += x
print(s)

s = 0
i = 0 
while( i < n ):
    s += l[i]
    i += 1
print(s)

print(badsum(n-1,l))

print(bettersum(l))