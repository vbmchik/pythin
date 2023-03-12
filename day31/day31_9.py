from logging import info, basicConfig, INFO
from threading import Thread
from time import sleep
import concurrent.futures


def thread_function(name):
    info(f"Thread {name} starting... ")
    sleep(2)
    info(f"Thread {name} stopped... ")


format = "%(asctime)s: %(message)s"
basicConfig(format=format, level=INFO, datefmt="%h:%M:%S")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #executor.map(thread_function, range(3))
    for x in range(3):
        executor.submit(thread_function,x)
print('done')
