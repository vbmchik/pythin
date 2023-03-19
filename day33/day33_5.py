from threading import Barrier, Thread
from time import sleep, time

br = Barrier(3)
store = []

def f1(x):
    print("Calc 1")
    
    sleep(1)
    store.append(x**2)
    br.wait()
    
def f2(x):
    print("Calc 2")
   
    sleep(2)
    store.append(x*2)
    br.wait()

Thread(target=f1, args=(3,)).start()
Thread(target=f2, args=(7,)).start()

br.wait()
print("Result: ", sum(store))
