import tkinter as tk
from pprint import pprint
from tkinter import messagebox


def on_off():
    global switch
    state = button_1["text"]
    if state == "On":
        state="Off"
    else:
        state="On"
    button_1["text"] = state
    if switch:
        label.unbind("<Button-1>")
        button_1.config(fg="red")
    else:
        label.bind("<Button-1>", peekbox)
        button_1.config(fg="black")
    switch = not switch


def peekbox(event=None):
    global word_no, words
    word_no+=1
    label.config(text=words[word_no%len(words)])


window = tk.Tk()
switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no=0
button_1 = tk.Button(window, text="On", command=on_off)
button_1.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1>", peekbox)
label.pack()
pprint(button_1)
window.mainloop()
