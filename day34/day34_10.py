def benchmark( func):
    
    import time

    def wrap(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time()-t)
        return res
    return wrap

def logger(func):
    
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, *args, **kwargs)
        return res
    return wrap

def counter(func):
    
    def wrap(*args, **kwargs):
        wrap.count +=1
        res = func(*args, **kwargs)
        print(func.__name__, wrap.count)
        return res
    wrap.count = 0
    return wrap


@benchmark
@logger
@counter
def rever(string):
    return string[::-1]

print(rever("а роза упала на лапу азора"))