import time

n = [0]


def cache(func):
    cache = {}

    def wrapper(x):
        if x in cache:
            return cache[x]
        cache[x] = func(x)
        return func(x)
    return wrapper


@cache
def fibonacci(n, l=n):
    if n == 15:
        l[0] = l[0] + 1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


start = time.perf_counter()
print(fibonacci(400))
print(f"executed {time.perf_counter()-start}")
print(n)
