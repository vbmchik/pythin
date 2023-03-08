import datetime


l = [1,2,3,4,5,4,3,2,1]
l = [x for x in range(1,90000000)]
print(datetime.datetime.now())
q = map(lambda x: x*x, l)
n = 0
for i in q:
    print(i)
    n += 1
    if n > 6:
        break
    
print(datetime.datetime.now())


r=[]
for x in l:
    r.append(x*x)
#print(r)
print(datetime.datetime.now())
print("aaa")