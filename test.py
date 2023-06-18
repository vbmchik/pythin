# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from collections.abc import Callable, Iterable, Mapping
from threading import Thread
import time
from tkinter import *
from tkinter.ttk import *
from typing import Any

class Myt(Thread):
    n = 0
    def __init__(self, text: StringVar, *args, **kwargs):
        super().__init__(None,args,kwargs)
        self.text = text
    
    def run(self) -> None:
        time.sleep(3)
        Myt.n +=1
        text.set("Attempt: " + str(Myt.n))
  

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
def dosomething():
    #time.sleep(9)
    t = Myt(text=text)
    t.start()



text = StringVar()
text.set("text")
label = Label(master,
              textvariable=text)


label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(master,
             text="Try to get data",
             command=dosomething )
btn1 = Button(master,
             textvariable=text)
btn.pack(pady=10)
btn1.pack(pady=30)

# mainloop, runs infinitely
mainloop()
