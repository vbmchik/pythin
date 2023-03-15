# Consumer потребитель проеряет доступность ресурса если нет то ждет оповещения от Producer


# Producer производитель что делает с ресурсм и когда ресурс свободен - оповещает метдом notify() 1 thread; notify_all() all threads
 
from threading import Condition, Thread
from queue import Queue
from time import sleep

cv = Condition()
q = Queue()

def order_making(name):
    while True:
        with cv:
            while q.empty():
                cv.wait()
                
            try:
                order = q.get_nowait()
                print(f"{name}: {order}")
                
                if order == "stop":
                    break
            except:
                pass
            sleep(0.5)
    print(f"{name} stop recieved!")
                
Thread(target=order_making, args=("thread1",)).start()
Thread(target=order_making, args=("thread2",)).start()
Thread(target=order_making, args=("thread3",)).start()
sleep(0.5)             
for i in range(10):
    q.put(f"order {i}")
with cv:
    cv.notify(3)
sleep(10)

for _ in range(3):
    q.put("stop")
with cv:
    cv.notify(3)

    