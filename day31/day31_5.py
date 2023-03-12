from threading import Thread
import math
from time import sleep, perf_counter
from solver import solve

mathlist = []
results = []


def mathprocess(value: str, pattern: str):
    #result = []
    #for x in range(1, 30001):
    #    r = solve(value.replace(pattern, str(x)))
    #    result.append(r)
    #results.append(result)
    result = list(map( lambda x: solve(value.replace(pattern, str(x))), range(1, 30001) ))
    results.append(result)
    print(f'done for {value}')


start_time = perf_counter()
mathlist.append("sin({x})*{x}")
mathlist.append("cos({x})*{x}")
mathlist.append("{x}*5-{x}*{x}")

threads = []

for s in mathlist: 
    t = Thread(target=mathprocess, args=(s,'{x}') )
    #mathprocess(s,'{x}')
    t.start()
    threads.append(t)

    


for t in threads:
    t.join()


end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
