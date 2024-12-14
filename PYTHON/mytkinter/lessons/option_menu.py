
import tkinter as tk


root = tk.Tk()
root.geometry("300x300")

options = [
    "Monday",
    "Tuesday",
    "Wednessday",
    "thursday",
    "friday"
    ]

def show(event):
    label = tk.Label(text=click.get()).pack()
    
click = tk.StringVar()
click.set(options[0])

drop = tk.OptionMenu(root,click,*options,command=show)
drop.pack()


root.mainloop()
