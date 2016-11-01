from tkinter import *
from tkinter import ttk

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)

t = Text(root, wrap=WORD)

def parse_reply(post):
    substring = post[:2]
    if substring == ">>":
        for i in range (2, len(post[2:])):
            if not post[i].isdigit():
                break
            substring += str(post[i])
            return substring
    else:
        return None

def insert_in_listbox(post):
    assert(post != None), "Parse string error!"

    reply = parse_reply(post)
    if reply != None:
        pass
        #colorize_reply(str)
    t.insert(END, post)
    t.insert(END, '\n')

def on_finish():
    scrollbar.pack(side="right", fill="y", expand=False)
    t.pack(side="left", fill="both", expand=True)
    root.mainloop()
