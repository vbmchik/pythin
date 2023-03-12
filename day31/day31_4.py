from threading import Thread
from time import sleep, perf_counter
from solver import solve

mathlist = []
results = []


def mathprocess(value: str, pattern: str):
    result = []
    for x in range(1, 10001):
        r = solve(value.replace(pattern, str(x)))
        result.append(r)
    print(f'done for {value}')


start_time = perf_counter()
mathlist.append("sin({x})*{x}")
mathlist.append("cos({x})*{x}")
mathlist.append("{x}*5-{x}*{x}")

for s in mathlist:
    mathprocess(s, '{x}')

end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
