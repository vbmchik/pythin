import tkinter as tk
from tkinter import Button, Checkbutton, Radiobutton, Label
def switchpro(*args):
    if switch.get() == 1:
        label["text"] = "1"
    else:
        label["text"] = "2"
    window.update_idletasks()
window = tk.Tk()
label = tk.Label(window, text = "Title lorem ipsum")
label.pack()
frame=tk.Frame(window, height=30, width=100, bg="#00009F")
frame.pack()
button = tk.Button(window, text="Button", command=lambda: switch.set(1-switch.get()))
button.pack(fill=tk.X)

switch = tk.IntVar(master=window, value=1)
switch.trace("w", switchpro)
switch.set(1)

checkbutton=Checkbutton(window, text="Check button", variable=switch)

checkbutton.pack()
entry = tk.Entry(window, width=30)
entry.pack()

rb_1 = Radiobutton(window, text="  0  ", variable=switch, value=0)
rb_2 = Radiobutton(window, text="  1  ", variable=switch, value=1)
rb_1.pack()
rb_2.pack()
rb_3 = Radiobutton(window, text="  0  ", variable=switch, value=0)
rb_4 = Radiobutton(window, text="  1  ", variable=switch, value=1)
rb_3.pack()
rb_4.pack()
switch.trace("w", switchpro)
window.mainloop()
