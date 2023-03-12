from threading import Thread
from time import sleep, perf_counter


def task():
    print("Starting a task...")
    sleep(3)
    print('Done')


start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)


t1.start()
t2.start()

print('started both threads!')


print('and waiting for results')

t = input("Input time to sleep")

t1.join()
t2.join()

end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
