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
button.pack(side=tk.RIGHT, fill=tk.Y)
button1 = Button(mywindows, text="Bye!", command=ButtonClick)
button1.pack()
button2 = Button(mywindows, text="Bye!", command=ButtonClick)
button2.pack()
button3 = Button(mywindows, text="Bye!", command=ButtonClick)
button3.pack()
mywindows.mainloop()
