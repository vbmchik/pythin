# найти степень числа используя рекурсию

n = 4
m = 6

def s(x,y):
    if y == 1:
        return x
    else:
        return s(x,y-1)*x
    
print(s(n,m))