#Третья задача

#Вычислите первые 100 чисел Фибоначчи. (Напишите код.)

# 1, 1, 2, 3, 5, 8, 13, 21

import math

def test():
    yield 1
    yield 2
    yield 3

def fib(n):
    a, b = -1, 0    
    while(n>0):
        yield b
        a, b = b, abs(a+b)
        n -= 1


def fib1():
    a, b = -1, 0
    while (True):
        yield b
        a, b = b, abs(a+b)



l = [x for x in fib(100)]
print(l)

l = fib1()

for _ in range(12):
    print(next(l))


