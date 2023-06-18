import tkinter as tk
from tkinter import messagebox

def on_off():
    global switch
    if switch:
        button_2.config(command=lambda : None)
        button_2.config(text="None!")
    else:
        button_2.config(command=peekbox)
        button_2.config(text="Peekbox")
    switch = not switch

def peekbox():
    messagebox.showinfo("", "Peekbox!")
    
window=tk.Tk()
switch=True
button_1 = tk.Button(window, text="On/Off", command=on_off)
button_1.pack()
button_2 = tk.Button(window, text="Peekbox", command=peekbox)
button_2.pack()
window.mainloop()