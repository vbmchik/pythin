import tkinter as tk
from tkinter import Button, messagebox
# GUI Graphical User Interface


def ButtonClick():
    warning = messagebox.askquestion("Quit?", "Are you sure?")
    if warning == "yes":
        mywindows.destroy()


mywindows = tk.Tk()
mywindows.title = "First application"
button = Button(mywindows, text="Bye!", command=ButtonClick)
button.grid(row=0,column=0)
button1 = Button(mywindows, text="Bye!", command=ButtonClick)
button1.grid(row=1, column=1)
button2 = Button(mywindows, text="Bye!", command=ButtonClick)
button2.grid(row=2, column=0, columnspan=3)
button3 = Button(mywindows, text="Bye!", command=ButtonClick)
button3.grid(row=3, column=2)
mywindows.mainloop()
