import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("500x500")
window.title('Frames')


note = ttk.Notebook(window)

tab1 = ttk.Frame(note)
label1 = ttk.Label(tab1, text='youre 1')
button1 = ttk.Button(tab1, text='click here1!')
button1.pack()
label1.pack() 

tab2 = ttk.Frame(note)
label2 = ttk.Label(tab2, text='youre 2')
button2 = ttk.Button(tab2, text='click here2!')
button2.pack()
label2.pack() 

tab3 = ttk.Frame(note)
label3 = ttk.Label(tab3, text='youre 3')
entry = ttk.Entry(tab3)
button3 = ttk.Button(tab3, text='click here3!')
entry.pack()
button3.pack()
label3.pack() 

note.add(tab1, text='TAB1', padding=9)
note.add(tab2, text='TAB2',padding=9)
note.add(tab3, text='TAB3',padding=9, )

note.pack()

window.mainloop()