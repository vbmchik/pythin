from solver import solve
from day34_home2 import logger

@logger("test.log")
def test1(x,y):
    return x+y


@logger("test.log")
def test2(st):
    return(solve(st))


@logger("test.log")
def test3(x):
    return x**3



print(test1(2,3))

print(test2("sin(30)"))
print(test3(5))