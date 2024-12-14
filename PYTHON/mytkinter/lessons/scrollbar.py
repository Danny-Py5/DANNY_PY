

from tkinter import (Tk,Listbox ,Scrollbar,RIGHT,
X,Y,LEFT,BOTH)


root = Tk()

listbox =  Listbox(root,selectmode="SINGLE")
listbox.pack(side=LEFT,fill=BOTH,expand=True)

scrollbar = Scrollbar(root)
scrollbar.pack(side=LEFT,fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.xview)

items = ["item "+str(val+1) for val in range(20)]
for  item in items:
    listbox.insert("end",item)

root.mainloop()


