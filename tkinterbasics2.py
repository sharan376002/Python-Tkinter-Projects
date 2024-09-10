import  tkinter as tk
from tkinter import ttk

def typesmoe():
    value = entry.get()
    label['text'] = value 
    print(label)
    #entry['state'] = 'disabled'

def changeOriginal():
    label['text'] = 'typeSomething'
    


#window


window = tk.Tk()
window.title("Checking")
window.geometry("300x250")

label = ttk.Label(master=window, text='typeSomething')
label.pack()

entry  = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Enter', command=typesmoe)
button1  = ttk.Button(master=window, text='chenge to orginal', command=changeOriginal)
button.pack()
button1.pack()





window.mainloop()