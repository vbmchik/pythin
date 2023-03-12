from logging import info, basicConfig, INFO
from threading import Thread
from time import sleep

def thread_function(name):
    info(f"Thread {name} starting... ")
    sleep(2)
    info(f"Thread {name} stopped... ")

format = "%(asctime)s: %(message)s"
basicConfig(format=format, level=INFO, datefmt="%h:%M:%S")

threads = []

for index in range(3):
    info(f'Main  : create and start thread {index}')
    x = Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()
    
for index, thread in enumerate (threads):
    info(f"Main joining thread {index}")
    thread.join() # wait for thread to finish
    info(f"Main - thread {index} done")
