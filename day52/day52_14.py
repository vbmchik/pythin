import tkinter as tk

windows = tk.Tk()

button_1 = tk.Button(windows, text="Button1")
button_1["anchor"] = tk.E
button_1["width"] = 20
button_1.pack(anchor=tk.E)
button_2 = tk.Button(windows, text="Button2")
button_2["anchor"] = tk.CENTER
button_2["width"] = 20
button_2["height"] = 3
button_2.pack(anchor=tk.SW)
windows.mainloop()
