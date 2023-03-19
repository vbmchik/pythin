import random
from threading import Thread


class MyOwnThread(Thread):

    def __init__(self, filename):
        Thread.__init__(self)
        self.filename = filename
   
  
    def run(self) -> None:
        r = [ random.randrange(1000)  for _ in range(1_000_000) ] 
        with open(self.filename, "w") as shfile:
            shfile.write(str(r))
        
        
l = []
for i in range(3):
    l.append(MyOwnThread(f"file{i}.txt"))  
for i in range(3):
    l[i].start()
for i in range(3):
    l[i].join()
    

 
