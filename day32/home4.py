
from threading import Lock, Thread


class MyOwnThread(Thread):

    def __init__(self, a: int, b: int, mlist: list):
        Thread.__init__(self)
        self.a = a
        self.b = b
        self.mlist = mlist

    def run(self) -> None:
       l = [ x for x in range(self.a, self.b)]
       if lock.acquire():
           self.mlist.extend(l)
           lock.release()
        
    
result = []
lock = Lock()
a = MyOwnThread(1, 1_000_001, result)
b = MyOwnThread(1_000_001, 2_000_001, result)
c = MyOwnThread(2_000_001, 3_000_001, result)
a.start()
b.start()
c.start()
a.join()
b.join()
c.join()
print(len(result))
