import tkinter as tk
from tkinter import ttk

def getmotion(event):
    print(f" X:{event.x}, Y:{event.y}")


#window
window = tk.Tk()
window.title("Event")
window.geometry("450x450")

#text
text = tk.Text(window)
text.pack()

#entry
entry = ttk.Entry(window,)
entry.pack()

#button
button = ttk.Button(window,text="button")
button.pack()

#   <modifier-type-detail>
window.bind("<Motion>",getmotion)
window.bind("<KeyPress>",lambda event: print(f" the key is pressed {(event.char)} "))
entry.bind("<FocusIn>",lambda event : print("The entry field is selected"))
entry.bind("<FocusOut>",lambda event : print("The entry field is  unselected"))
text.bind("<MouseWheel>",lambda event : print("the mousewell is going upp and down"))


window.mainloop()