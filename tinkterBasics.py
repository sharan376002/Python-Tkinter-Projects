import tkinter as tk
from tkinter import ttk

def sayhello():
    print("hello")

window = tk.Tk()
window.title("HELLO")
window.geometry("300x300")


label = ttk.Label( master=window, text="My label")
label.pack()

entry = ttk.Entry( master=window)
entry.pack()

button = ttk.Button(master=window , text="say Hello", command=sayhello)  # lambada : print('hello)
button.pack()


window.mainloop()