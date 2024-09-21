import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("500x500")
window.title('Frames')

#frames
frames = ttk.Frame(window, width=100, height=220, borderwidth=20, relief=tk.RIDGE)
frames.pack_propagate(True)
frames.pack()

#parent
label = ttk.Label(frames, text='HOME')
label.pack()

button = ttk.Button(frames , text='Speed',command=lambda:print("button pressed"))
button.pack()

window.mainloop()