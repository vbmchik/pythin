def decor(func):
    print("1")
    def wrap(*args, **kwargs):
        print("2")
        return func(*args, **kwargs)
    return wrap

def func(a,b):
    return(a+b)

wr = decor(func)

print(wr(2,3))

@decor
def f(c,t):
    return c-t

print(f(2,3))

def rp():
    return print

rp()("dfdfdf")