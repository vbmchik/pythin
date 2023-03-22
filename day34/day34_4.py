import time
import math

def calculate_time(func):
    
    def inner( *args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Overall time {func.__name__}: {end-begin}")
    return inner

@calculate_time
def factorial(num):
    time.sleep(1)
    print(math.factorial(num))
    
factorial(12)