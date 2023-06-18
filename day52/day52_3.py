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
button.place(x=10, y=10, width=150)
button1 = Button(mywindows, text="Bye!", command=ButtonClick)
button1.place(x=30, y=50, width=50)
mywindows.mainloop()
