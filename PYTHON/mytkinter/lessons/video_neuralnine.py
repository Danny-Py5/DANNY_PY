

import tkinter as tk

class MyApp:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x700+760+0")

        self.label = tk.Label(self.root,text="Your message")
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,width=500,height=10,font=("Times New Roman",18))
        self.textbox.pack(padx=10,pady=10)

        self.checkstate = tk.IntVar()

        self.check = tk.Checkbutton(self.root,text="show messagebox",font=("Arial",12),
                                    variable=self.checkstate,cursor="hand2")
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root,text="Show message",font=("Arial",12),command=self.show_message)
        self.button.pack(padx=10,pady=10)
        self.root.mainloop()

    def show_message(self):
        if self.checkstate.get() == 0:
            print(self.textbox.get(1.0,tk.END),end="")
        else:
            __import__("tkinter").messagebox.showinfo("info",self.textbox.get(1.0,tk.END))
        


MyApp()

