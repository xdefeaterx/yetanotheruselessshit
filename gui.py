from tkinter import *
from tkinter import ttk

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

def insert_in_listbox(str):
    listbox.insert(END, str)
    listbox.insert(END, '\n')

def on_finish():
    listbox.pack(side=LEFT, fill=BOTH, expand=TRUE)
    scrollbar.config(command=listbox.yview)
    root.mainloop()
