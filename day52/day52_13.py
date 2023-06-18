import tkinter as tk

windows = tk.Tk()
string = "Quick brown fox jumps over lazy dog!"
label_1 = tk.Label(windows, text=string)
label_1.grid(column=0,row=0)
label_2 = tk.Label(windows, text=string, font=("Times", "22"))
label_2.grid(column=0,row=1)
label_3 = tk.Label(windows, text=string, font=("Arial", "45", "bold"))
label_3.grid(column=0,row=2)
windows.mainloop()