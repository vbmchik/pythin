# bind()
# windget.bind(ebent, callback)

import tkinter as tk
from tkinter import messagebox

def click(event=None):
    tk.messagebox.showinfo("Click!", "It was a click!")
    label.destroy()
    
def blink(event=None):
    if frame["bg"] == "blue":
        frame["bg"] = "grey"
    else:
        frame["bg"] = "blue"
        
def aback(event=None):
    frame.config(bg="blue")
    frame.after(500, blink)

def pback(event=None):
    frame.config(bg="red")

window = tk.Tk()
label = tk.Label(window, text="Text label!")
label.bind("<Button-1>", click)
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="red")
frame.bind("<Enter>", aback)
frame.bind("<Leave>", pback)
frame.pack()

window.mainloop()
