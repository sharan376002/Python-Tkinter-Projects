import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("450x450")
window.title("Canvas")

canvas = tk.Canvas(window, bg="#c4ff33")
canvas.pack()
                                                                    # here 2 is the gap of the dash and 4 is distance between of them
canvas.create_rectangle((20,20,100,100), fill="red", width=3, dash=(2,4)) # left, top , right, bottom
canvas.create_line((10,10,340,340),fill="blue",width=1)  # start_x,start_y,end_x,end_y
canvas.create_oval((60,60,150,150), fill="#33ff9c", width=0.8,)# left, top , right, bottom
canvas.create_polygon((39,39,190,180, 350,390 ),fill="blue",width=1) # (x1,y1) ,(x2,y2), (x3,y3)
canvas.create_arc(
 	(200, 0, 300, 100), 
 	fill = 'red', 
 	start = 45, 
 	extent = 140, 
 	style = tk.CHORD, 
 	outline = 'red', 
	width = 1)
canvas.create_text((100,200), text = 'this is some text', fill = 'green', width = 10)
canvas.create_window((150,100), window = ttk.Button(window, text= 'this is text in a canvas'))
 

window.mainloop()