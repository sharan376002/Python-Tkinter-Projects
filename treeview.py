import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry("600x400")
window.title("Tables")

book_name = ["Blinders","Investor", "Great", "MBA", "Stoic"]
name_book = ["thomas", "ben", "Robert", "grant", "Josh kalfman", "Seneca"]
price_book = [price for price in range(100, 155)]


tabel = ttk.Treeview(window, columns=('Book','Author', 'Price'), show="headings")
tabel.heading('Book',text='BOOK')
tabel.heading('Author',text='AUTHOR')
tabel.heading("Price", text='PRICE')
tabel.pack()

#inset the values into the tabel

#tabel.insert(parent="", index=0, values=("blinders","john",price_book[1]))
for i in range(100):
    Book = choice(book_name)
    Author = choice(name_book)
    price = choice(price_book)
    data = (Book,Author,price)
    tabel.insert(parent="", index=0 , values=data)


# events
def item_select(_):
	print(tabel.selection())
	for i in tabel.selection():
		print(tabel.item(i)['values'])
	# table.item(table.selection())

def delete_items(_):
	print('delete')
	for i in tabel.selection():
		tabel.delete(i)

tabel.bind('<<TreeviewSelect>>', item_select)
tabel.bind('<Delete>', delete_items)







window.mainloop()