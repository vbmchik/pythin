# bind()
# windget.bind(ebent, callback)

import tkinter as tk
from tkinter import messagebox


def click(event=None):
    if event == None:
        tk.messagebox.showinfo("Click!", "It was a click!")
    else:
        string = "x=" + str(event.x) + ", y=" + str(event.y) + \
            ", num=" + str(event.num) + ", type=" + event.type
        messagebox.showinfo("EVent!", string)

def aback(event=None):
    frame.config(bg="blue")


def pback(event=None):
    
    frame.config(bg="red")


window = tk.Tk()
label = tk.Label(window, text="Text label!")
label.bind("<Button-1>", click)
label.bind("<Button-2>", click)
label.bind("<Button-3>", click)
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="red")
frame.bind("<Enter>", aback)
frame.bind("<Leave>", pback)
frame.pack()

window.mainloop()
