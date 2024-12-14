#import datamanagement.file_manager.fm_operation as fm
import os
import tkinter as tk
from tkinter import messagebox as msg


class NoteTaking:
    def __init__(self,root):
        self.root = root
        root.title("Note Taking")
        root.geometry("515x430")
        root.resizable(False,False)

        self.save_button = tk.Button(root,text= "New Save")
        self.save_button.place(x=5,y=2)
        self.save_button.bind("<Button-1>",self.__Save)
        
        self.search_button = tk.Button(root,text= "Search")
        self.search_button.place(x=450,y=2)
        
        self.text_widget = tk.Text(root,width=50, height=20,font=("Times New Roman",14))
        self.text_widget.place(x=5,y=40)

        self.open = tk.Button(root,text="Open")
        self.open.place(x=210,y=3)
        self.open.bind("<Button-1>",self.__open)

    def __open(self,event):
        new = tk.Toplevel(self.root)
        all_file_label = tk.Label(new,text="All Files:")
        all_file_label.pack(padx=10, pady=0)

        self.file_name = []
        for num,val in enumerate(os.listdir(),start=1):
            if "." in val:
                continue
            self.file_name.append(val)
            self.val = tk.Button(new,text=val,command=lambda:self.click(val))
            self.val.place(x=0,y=num*22)
        
    def click(self,file_name):
        self.text_widget.delete(1.0,tk.END)
        self.text_widget.insert(tk.END,str(file_name))

    def __Save(self,event):
        # create a new window
        self.new_window = tk.Toplevel(self.root)
        #self.new_window.resizable(False,False)
        self.new_window.geometry("300x200")
        
        self.filename = tk.Label(self.new_window,text="File Name:")
        self.filename.place(x=0,y=50)

        self.file_name_entry = tk.Entry(self.new_window)
        self.file_name_entry.place(x=80,y=52)

        # save and cancel btn
        save = tk.Button(self.new_window,text="Save", command = self.save)
        save.place(x=70,y=100)
        cancel = tk.Button(self.new_window,text="Cancel",command=self.new_window.destroy)
        cancel.place(x=200,y=100)

    def save(self):
        fn = self.file_name_entry.get()
        if fn == "":
            msg.showwarning("Warning","File name is empty!")
            return 
        for val in os.listdir():
            if val == fn:
                msg.showwarning("Warning","File already exist!")
                return
        else:
            text = self.text_widget.get(1.0,tk.END)
            with open(fn,"w",encoding="UTF-8") as f:
                f.write(text)
                msg.showinfo("Information","file saved")
                self.new_window.destroy()
                return
        
    
def main():
    root = tk.Tk()
    note = NoteTaking(root)
    root.mainloop()

if __name__ == "__main__":
    main()
