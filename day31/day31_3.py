from threading import Thread
from time import sleep, perf_counter


def task(id):
    print(f"Starting a task... {id}")
    sleep(3)
    print(f'Done {id}')


start_time = perf_counter()

threads = []

for n in range(1,11):   # 
    th = Thread(target=task, args=(n,))
    threads.append(th)
    th.start()


print('started all threads!')

for t in threads:
    t.join()

end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
