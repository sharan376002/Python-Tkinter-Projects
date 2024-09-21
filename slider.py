import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


window = tk.Tk()
window.title("slider")
window.geometry("600x600")

scale_float = tk.DoubleVar()
slider = ttk.Scale(window,command=lambda value: print(scale_float.get()),from_=0,to=100, length=300, orient ='vertical', variable=scale_float)
slider.pack()


# progress bar
progress = ttk.Progressbar(
	window, 
	variable = scale_float, 
	maximum = 25,
	orient = 'horizontal',
	mode = 'determinate',
	length = 400)
progress.pack()


scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()


exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, orient = 'vertical', variable = exercise_int)
exercise_progress.pack()
exercise_progress.start()

label = ttk.Label(window, textvariable = exercise_int)
label.pack()

exercise_scale = ttk.Scale(window, variable = exercise_int, from_ = 0, to = 100)
exercise_scale.pack()




window.mainloop()