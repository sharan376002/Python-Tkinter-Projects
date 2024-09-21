import tkinter as tk
from tkinter import ttk


window =tk.Tk()
window.title("comboBox ad Spin Box")
window.geometry("350x250")

#combobox

combo_label = ttk.Label(window,text='Choose any progamming language')
combo_label.pack()


languages = ['Chaincode',"c","c++","python","java","ruby","rust","sql","javascript"]
combo_var = tk.StringVar(value= languages[0])

comboBox = ttk.Combobox(window , textvariable=combo_var)
comboBox['value']= languages  # also, comboBox.configu(values=items)
comboBox.pack()

label_2 = ttk.Label(window)


comboBox.bind('<<ComboboxSelected>>', lambda event : label_2.config(text=f'Selected Text : {combo_var.get()}'))
label_2.pack()



window.mainloop()