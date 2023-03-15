from threading import Thread,  RLock
from time import sleep


def unlock():
    try:
        lock1.release()
    except Exception as ex:
        print("Thread error ",ex)


lock = RLock()
lock1 = RLock()

lock.acquire()
lock1.acquire()

sleep(2)

t = Thread(target=unlock)
t.start()

sleep(2)

lock.release()
try:
    lock1.release()
except Exception as ex:
    print(ex)
