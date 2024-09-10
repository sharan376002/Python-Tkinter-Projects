import tkinter as tk
from tkinter import ttk


window =tk.Tk()
window.title("spinbox")
window.geometry("450x450")

label =ttk.Label(window,text='choose the age:')
label.pack()
spin_int = tk.IntVar(value=2)
spin = ttk.Spinbox(window, from_=1, to=100, command=lambda:print(spin_int.get()), textvariable=spin_int) #tthis function also have the increament 
spin.pack()

spin.bind('<<Increment>>', lambda event: print("up"))
spin.bind('<<Decrement>>', lambda event: print("down"))



label1 =ttk.Label(window,text='choose the age:')
label1.pack()

lang= ("a","C","b","e","f")
spin_var = tk.StringVar(value=lang[0])
spin1 = ttk.Spinbox(window,command=lambda:print("value selected"), textvariable=spin_var) #tthis function also have the increament 
spin1.pack()





window.mainloop()