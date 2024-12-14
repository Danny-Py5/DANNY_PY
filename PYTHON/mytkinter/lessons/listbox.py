
import tkinter as tk

root = tk.Tk()
root.geometry("100x400+1100+0")

def add_items():
    new_entry = entry.get()
    if new_entry:
        lb.insert(tk.END,new_entry)
        entry.delete(0,tk.END)

def delete_item():   
    selected_indices = lb.curselection()

    try:
        selected_item = selected_indices[0]#[lb.get(index) for index in selected_indices]
        lb.delete(selected_item)
    except IndexError:
        pass 

lb =  tk.Listbox(root,selectmode=tk.MULTIPLE)
lb.pack()

entry = tk.Entry(root)
entry.pack()

add_btn = tk.Button(root,text="Add",command=lambda:add_items())
add_btn.pack()

del_btn = tk.Button(root,text="Del",command=lambda:delete_item())
del_btn.pack()


root.mainloop()

###create a listbox
##lb = Listbox(root,selectmode=tk.SINGLE)# selectmode = SINGLE allows selecting one  item at a time
##lb.pack()
##
### add items to the Listbox
##items = ["Item1","Item2","Item3","Item4"]
##for item in items:
##    Listbox.insert(tk.END,item)
##

##def add_items(items):
##    for item in items:
##        lb.insert(tk.END,item)
##
##items = ["Item1","Item2","Item3","Item4"]
##lb =  tk.Listbox(root,selectmode=tk.SINGLE)
##lb.pack()
##add_items(items)


