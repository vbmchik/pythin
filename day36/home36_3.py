import time
from functools import cache


def decor_time(func):
    def wrap(*args, **kwargs):
        if (kwargs["timer"]):
            start = time.perf_counter()
        result = func(*args, **kwargs)
        if (kwargs["timer"]):
            print(f"{func.__name__} elapsed {time.perf_counter()-start}")
        return result
    return wrap


#@decor_time
def fibonacci(n, timer=True):
    if n < 2:
        return n
    return fibonacci(n-1, timer=False) + fibonacci(n-2, timer=False)


# decor_time(fibonacci)(30)
d = decor_time(fibonacci)
d(30, timer=True)
#fibonacci(30, timer=True)
