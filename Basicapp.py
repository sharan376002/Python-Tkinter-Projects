import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


#Window
window = tk.Tk()
window.title("Testing")
window.geometry("400x400") # widthX height

#title

title_label = ttk.Label(master= window, text='live bus Tracker')
title_label.pack()


#input frame

input_frame = ttk.Frame( master= window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="Search")
entry.pack(side='left', padx="10")
button.pack(side='left')
input_frame.pack(pady=10)







#Run
window.mainloop()