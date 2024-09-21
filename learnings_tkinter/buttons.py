import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("350x200")
window.title("Buttons")

button_var = tk.StringVar(value="button")
button = ttk.Button(master=window, text="button",textvariable=button_var)
button.pack()

radio_var = tk.StringVar(value="radio")
radio = ttk.Radiobutton(master=window, text= "radio",textvariable=radio_var)
radio.pack()

radio1 = ttk.Radiobutton(master=window, text= "radio+", value="radio1")  # in the radio button we must add the value 
radio1.pack()

radio2 = ttk.Radiobutton(master=window, text= "radio+", value="radio2")
radio2.pack()


"""
    check_var = tk.IntVar(value=7)
    check = ttk.Checkbutton(master=window, 
                            text="check", 
                            variable=check_var,
                            command=lambda:print(check_var.get())
                            ,onvalue=3
                            ,offvalue=7)
    check.pack()
"""

def radiofunc():
    print(check_var.get())


radio_var1 = tk.StringVar()
radioA = ttk.Radiobutton(window, text="radio A",textvariable=radio_var1 , command=radiofunc)
radioA.pack()

radioB = ttk.Radiobutton( window, text= "radio B",textvariable=radio_var1, command=radiofunc)
radioB.pack()

check_var = tk.BooleanVar()
check = ttk.Checkbutton(window, 
                        text="checkbox",variable=check_var,command=lambda:print(radio_var1.get()))

check.pack()





window.mainloop()