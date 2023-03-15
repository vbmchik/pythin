# -20 20 step 0.001 считает какую то сложную функцию 
# 40000 - 4 core
# -20  -10  
# -10    0
#   0   10
#  10   20
# GIL Global Interpreter Lock
# CPython
#
# CPU - bound - Process
# IO - bound  - Thread
#
#

from threading import Thread
from time import sleep

def func(number):
    print(f"I am func number {number}! ")
    sleep(3.4)
   
l = [ Thread(target=func, args=(x,)) for x in range(100) ]
for t in l :
    t.start()
for t in l :
    t.join()
