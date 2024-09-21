import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x500")
window.title(" Drawing canva")


canvas = tk.Canvas(window)
canvas.pack()

def movefunc(event):
    x= event.x
    y=event.y
    canvas.create_oval(x-brush_size/2,y-brush_size/2,x+brush_size/2,y+brush_size/2 , fill='#000000')

def brushadj(event):
    global brush_size

    if event.delta >0:
        brush_size +=4
    else:
        brush_size -=4
    brush_size = max(0, min(brush_size,50))    


brush_size = 2
canvas.bind('<Motion>',movefunc)
canvas.bind('<MouseWheel>',brushadj)


window.mainloop()