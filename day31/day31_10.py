from multiprocessing import freeze_support, get_context
from threading import Thread
import math
from time import sleep, perf_counter
from solver import solve
from multiprocessing import Process
import concurrent.futures.process



mathlist = []
results = []


def mathprocess(value: str):
    # result = []
    # for x in range(1, 30001):
    #    r = solve(value.replace(pattern, str(x)))
    #    result.append(r)
    # results.append(result)
    pattern = '{x}'
    result = list(
        map(lambda x: solve(value.replace(pattern, str(x))), range(1, 30001)))
    results.append(result)
    print(f'done for {value}')


if __name__ == '__main__':
    freeze_support()
freeze_support()

start_time = perf_counter()
mathlist.append("sin({x})*{x}")
mathlist.append("cos({x})*{x}")
mathlist.append("sin({x})*{x}")

p = get_context("fork").Pool(3)
results = p.map(mathprocess, mathlist)
p.close()

    

end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
start_time = perf_counter()
with concurrent.futures.ThreadPoolExecutor(4) as executor:
    f = executor.map(mathprocess, mathlist)
    


end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
