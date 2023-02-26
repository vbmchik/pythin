#numbers = [19, 2, 10, 8, 2]
# [(0,19),(1,2),(2,10),...]

#print(numbers.index(10,1,3))

#l = []

#for i in range(1,10):
#    l.append(i)
 
def check(x):
    return x%2
   
l = [ i for i in range(1,10) ]    
print(l)

p = list(filter(lambda x:  x % 2, l))
print(p)

m = list(map(lambda x: x**2, filter(lambda x:  x % 2, l)))

print(m)