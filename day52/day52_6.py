import tkinter as tk
from tkinter import Button, messagebox
# GUI Graphical User Interface


def ButtonClick():
    warning = messagebox.askquestion("Quit?", "Are you sure?")
    if warning == "yes":
        mywindows.destroy()

# #000000
# #FFFFFF
mywindows = tk.Tk()
mywindows.title = "First application"
button = Button(mywindows, text="Bye!", bg="red",
                fg="#CF0F12", command=ButtonClick)
button.pack()
mywindows.mainloop()
