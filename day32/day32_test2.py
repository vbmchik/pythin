from threading import Thread, RLock
from time import sleep


class TestA(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name=name

    def run(self):
        print(f"Thread {self.name}")   
        print(f"Thread {self.name} tries to open lock")
        try:
            lock.release() 
            print(f"Thread {self.name} opened lock")
        except Exception as e:
            print(str(e))
           
        lock.acquire()
        print(f"Thread {self.name} locking locked lock")
        sleep(5)
        print(f"Thread {self.name} opened locked lock")
        lock.release()
        

lock = RLock()
TestA("Petya").start()
sleep(1)
TestA("Yasha").start()
