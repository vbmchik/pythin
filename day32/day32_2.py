from threading import Thread
from time import sleep

class MyOwnThread(Thread):
    def __init__(self, limit):
        Thread.__init__(self)
        self._limit = limit
    
    def run(self) -> None:
        for i in range(self._limit):
            print(f'thread {i}')
            sleep(0.5)

mythread = MyOwnThread(8)
mythread.start()