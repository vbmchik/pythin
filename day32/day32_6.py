from threading import Thread, Lock
from time import sleep

def unlock():
    lock1.release()

lock = Lock()
lock1 = Lock()

lock.acquire()
lock1.acquire()

sleep(2)

t = Thread(target=unlock)
t.start()

sleep(2)

lock.release()
try:
    if lock1.locked():
        lock1.release()
except Exception as ex:
    print(ex)
    
