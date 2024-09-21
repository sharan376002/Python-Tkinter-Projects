import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def sayhello():
    print("hello")

def alert_driver():
    messagebox.showwarning(window,"Speed Alert")


window = tk.Tk()
window.title("HELLO")
window.geometry("300x300")


label = ttk.Label( master=window, text="My label")
label.pack()

entry = ttk.Entry( master=window)
entry.pack()

button = ttk.Button(master=window , text="say Hello", command=alert_driver)  # lambada : print('hello)
button.pack()


window.mainloop()