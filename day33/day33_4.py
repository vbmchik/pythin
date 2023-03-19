from threading import Thread
from time import sleep


class MyOwnTimer(Thread):
    def __init__(self, limit, action):
        Thread.__init__(self)
        self.limit = limit
        self.action = action

    def run(self) -> None:
        sleep(self.limit)
        self.action()


mythread = MyOwnTimer(8, lambda: print("Timer started!"))
mythread.start()
