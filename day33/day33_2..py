from threading import Thread, Event
from time import sleep, time

event = Event()

def runner(name: str):
    event.wait()
    print(f"{name}")
    
runners = [Thread(target=runner, args=(f"runner{i}",)) for i in range(10)]
for d in runners:
    d.start()
    
event.set()