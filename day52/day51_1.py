import tkinter as tk
from tkinter import Button
#GUI Graphical User Interface
#def ButtonClick():
#    mywindows.destroy()
    
mywindows = tk.Tk()
mywindows.title = "First application"
button = Button(mywindows, text="Bye!", command=mywindows.destroy)
button.place(x=10, y = 10)
mywindows.mainloop()