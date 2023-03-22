""" есть очередь - потоков клиентов ночного клуба(300) их пропускают барьером по 15 человек
на столе бочонок пива одновременно налить может только один человек(наливается пиво 1 секунду)
человек решает хочет или не хочет пива с вероятностью 50 процентов
 """
 
import random
from threading import Barrier, Lock, Thread
from time import sleep


class Client(Thread):
    
    def __init__(self, name) -> None:
        Thread.__init__(self)
        self.name = name

    def run(self) -> None:
        print(f"Client {self.name} is waiting to enter the club")
        security.wait()
        print(f"Client {self.name} is inside the club thinking if he wanna drink")
        choice = random.randint(0,1)
        if choice:
            beer.acquire()
            print(f"Client {self.name} is pour beer")
            sleep(1)
            beer.release()
            print(f"Client {self.name} is drinking beer")
            sleep(5)     
        print(f"Client {self.name} is dancing")
        sleep(10)
        if choice:
            print(f"Client {self.name} is in the waiting room")
            sleep(5)
        print(f"Client {self.name} is leaving")
        
        

        
security = Barrier(15)
beer = Lock()

tail = [ Client(f"client{x}") for x in range(300)]
for client in tail:
    client.start()