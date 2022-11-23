


#Map 

def sq(squares):
    for i in range(1,30,2):
        squares.append(i**i)
    return squares

def q(k,v):
    return k*v
def l(a,b):
    return [a,b]

squares = []
#print(sq(squares))
#result = map(q, range(1,10,1))
result = map(q, range(1,10,1), range(1,10,2))
print(list(result))
#result1 = map( lambda x: x**3, range(1,10,1))
result2 = map( lambda x, y: [x,y] if x > y else [y,x], range(1,10,1), [1,3,2,5,4,3,7,9,8])
result3 = map( lambda x, y, z  : [x > y, x > z], range(1,10,1), [1,3,2,5,4,3,7,9,8], [5,3,4,5,6,3,1,3,5])
result4 = map( lambda x: x%2==0, [1,2,3,4,5,6,7,8,9])
# map( преобразование, последовательности )

print(list(result4))