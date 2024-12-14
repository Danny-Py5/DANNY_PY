

import tkinter as tk


def file_new():print("file new")

def save():print("save")

root = tk.Tk()
root.geometry("300x500+860+0")
#menu_bar = tk.Menu(root)

#file_menu = tk.Menu(menu_bar,tearoff=0)
##menu_bar.add_cascade(label="File",menu=file_menu)
##
##
##file_menu.add_command(label="New",command=file_new)
##file_menu.add_command(label="Save",command=save)

# configure the  main window to use the  menu bar 
#root.config(menu=menu_bar)



menu_bar = tk.Menu(root)

filemenu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Save",menu=filemenu)

filemenu.add_command(label="New save",command=save)

root.config(menu=menu_bar)



root.mainloop()
