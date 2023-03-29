import time
from functools import lru_cache
from functools import cache


#@lru_cache(maxsize=300)
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


start = time.perf_counter()
print(fibonacci(400))
print(f"executed {time.perf_counter()-start}")
