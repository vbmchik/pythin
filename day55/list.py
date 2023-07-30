from threading import Thread
import time
from tkinter import * 

def somefunc():
    for values in range(100):
        listbox.insert(END, values)
        time.sleep(1)
        


root = Tk()
  
listbox = Listbox(root)
  
# Adding Listbox to the left
# side of root window
listbox.columnconfigure(0,weight=3)
listbox.pack(side = LEFT, fill = BOTH, expand=1)
  

scrollbar = Scrollbar(root)
  

#scrollbar.pack(side = RIGHT, fill = BOTH)
scrollbar.pack(side=RIGHT, fill=BOTH)
  
t = Thread(target=somefunc)
# Insert elements into the listbox
t.start()
      
# Attaching Listbox to Scrollbar
# Since we need to have a vertical 
# scroll we use yscrollcommand
listbox.config(yscrollcommand = scrollbar.set)
  
# setting scrollbar command parameter 
# to listbox.yview method its yview because
# we need to have a vertical view
scrollbar.config(command = listbox.yview)
  
root.mainloop()