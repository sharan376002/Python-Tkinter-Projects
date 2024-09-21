import tkinter as tk
import ttkbootstrap as ttk


def EvenOrOdd():

    num = int(entry.get())
    if num% 2==0:
        output_string.set("it is a Even")
    else:
        output_string.set("it is a Odd")
    

window = tk.Tk( )
window.title("EVEN OR ODD")
window.geometry("400x200")

title_label = ttk.Label(master = window  , text ="Check Even OR ODD")
title_label.pack()

#input
input_frame = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryInt )
button = ttk.Button(master=input_frame , text="Check",  command= EvenOrOdd)
entry.pack(side='left',padx=10 )
button.pack(side='left',padx=10)
input_frame.pack(pady =10)

#output
output_string = tk.StringVar()
output_Label = ttk.Label(master = window, 
                   text = 'output',
                   font = 'calibri 24',
                   textvariable = output_string)
output_Label.pack(pady=10)










#run
window.mainloop()
