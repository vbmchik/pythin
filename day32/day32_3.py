# a = a + result a = 5
# 6 11 -> a
# 12 17->a 
# 17 - 23

from threading import Thread, Lock
from time import sleep

lock = Lock()
stop_thread = False

def ant(number):
    print('Ant never get tired! Start working!')
    while True:
        print(f"--> ant {number} works!")
        if lock.acquire(blocking = True, timeout=3):
            if stop_thread is True:
                lock.release()
                break
            lock.release()
        sleep(0.5)
    print(f"Somebody stopped ant {number} !")

t = Thread(target=ant,args=(1,),daemon=True)
t1 = Thread(target=ant,args=(2,),daemon=True)
t.start()
t1.start()
sleep(2)
lock.acquire()
stop_thread = False
print("Stop threads!")
sleep(5)
lock.release()
sleep(5)
lock.acquire()
stop_thread = True
print("Stop threads!")
sleep(10)
lock.release()

print("Oi!")