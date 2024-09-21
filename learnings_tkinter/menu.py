import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("500x500")
window.title('Frames')


menu = tk.Menu(window)

file_menu = tk.Menu(menu,tearoff=False)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='More..')

menu.add_cascade(label="Home", menu=file_menu)




window.configure(menu = menu)

window.mainloop()