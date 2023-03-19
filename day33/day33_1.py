# семафор

import random
from threading import Semaphore, Thread
from time import sleep, time
ticket_office = Semaphore(value=3)

def ticket_buyer(number):
    start_service = time()
    with ticket_office:   # ticket_office.require()
        print(f"client {number} started having fun")
        sleep(random.randint(1,5))
        print(f"client {number} service time = {time()-start_service}")
    
buyers = [ Thread(target=ticket_buyer, args=(i,)) for i in range(15) ]    
for b in buyers:
    b.start()
