import tkinter as tk
from tkinter import ttk
 
def start():
    str_var.set("Test")


#window
window = tk.Tk()
window.title("strVAr")
window.geometry("300x250")

# sring Var
str_var = tk.StringVar()

label = ttk.Label(master=window, text='typeSomething', textvariable=str_var,)
label.pack()

entry  = ttk.Entry(master=window, textvariable=str_var)
entry.pack()

entry  = ttk.Entry(master=window, textvariable=str_var)
entry.pack()

button = ttk.Button(master=window, text='Enter' , command=start)
button.pack()





window.mainloop()