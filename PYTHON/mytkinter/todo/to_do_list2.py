
from tkinter import ttk
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox as mg



WIDTH = 400
HEIGHT=700
INPUT_FRAME_COLOR = "azure"
BACKGROUND_COLOR = "midnightblue"
ENABLE_ADD_MESSAGE = True
ENABLE_EMPTY_MESSAGE = True
HELP_NOTE = '''
****** Welcome  to "To-Do List" App *******
           Your personal Task Manager
           --------------------------

Developer: Danny_Py
Date:      Sunday 7, Dec. 2023
copyright: @2023

1. Getting Started.
   ---------------
   - Upon opening the app, you will find a
     clean and straightforward interface.
     The main screen displays you task list.

2. Adding a Task:
   --------------
   - To add a task, simply write your task
     description in the entry box and click
     on the "ADD" button or press the ENTER key.

3. Deleting Tasks:
   ---------------
   - To delete a task, click on the task you
     want to delete and click the "DELETE" button.
     You will see a popup, which says "Task Delete"

4. Other:
   -----

    Menu Bar.
    ----------------
    1. <Option> Menu:
            *  Close without question:
               ----------------------
               Allows you to close the App without
               showing any popup
               
            * Delete All Tasks:
              -----------------
              Choosing this command will delete and
              clear all your tasks list
              
    2. <Setting> Menu.
            * Add Task Without Message:
              ------------------------
              Add Task Without Message allows you 
              to disables the "Task Added" Popup
              when a new task is added.

            * Add Task With Message:
             -----------------------
              This command Enables the "Task Added"
              Popup when a new task is added.
              
            * Disable Entry Warning:
              ---------------------
              This command disables the popup
              that shows when the "ADD" button is
              clicked and the task entry is
              empty.
              
            * Enable Entry Warning:
              --------------------
              It enables the entry warning
              
    3. <Theme> Menu: this menu allows you to change the
       background of your app
            * Light blue: -> Turns the background colour
              to light blue

            * White: -> Turns the background colour to
              white.

    Enjoy your productivity boost

    To-Do list is designed to simplify your  task
    management. Stay organized, meet deadlines,
    and accomplish more each day.'''

class Base:
    '''the base class'''
    
    def __init__(self,root):    
        self.root = root
   
        
    def add_task(self,task_entry,list_box):
        
        new_entry= task_entry.get().title()
        if len(new_entry) > 35:
            mg.showinfo("Info",__import__("random").choice(["Task description should be descriptive\nand short",
                        "Task description too long!"]))
            return
        
        if new_entry:
            list_box.insert(tk.END,new_entry)
            try:
                with open("task_list.txt","a") as f:
                    f.write(new_entry)
                    f.write("\n")

                # delete the entry box
                task_entry.delete(0,"end")
                # show the needful message
                if ENABLE_ADD_MESSAGE == True:
                    mg.showinfo("Add task","Task Added!")
            except:
                task_file = open("task_list.txt","w",encoding="UTF-8")
                task_file.close()   
        else:
            if ENABLE_EMPTY_MESSAGE == True:
                mg.showwarning("Warning","Task entry is\nEmpty")

    def delete_task(self,list_box):
        '''delete selected task from task_file  and listbox'''
        selected_indices = list_box.curselection()
        if selected_indices: # prevent IndexError
            selected_task_index = int(selected_indices[0])
            selected_task = list_box.get(selected_task_index)

            question = mg.askyesnocancel("Question","Are you sure you want to\ndelete {}?".format(selected_task))
            if question:
                file = "task_list.txt"
                # get all tasks from task file
                try:
                    with open(file,"r",encoding="UTF-8") as f:
                        updated = [val.strip() for val in f if val !="\n"]           
                        with open(file,"w",encoding="UTF-8") as f:
                            for val in updated:
                                if val == selected_task:
                                    continue
                                f.write(val+"\n")
                    
                    list_box.delete(selected_task_index)
                    mg.showinfo("Info","Task deleted")
                except:
                    mg.showerror("File Error","Unfortunately task not deleted\n\nWHY?: It seems you have deleted the task file or the task file has been currupted.\n\nWe are very sorry about this.\n\n-To solve this, Click the 'ok' button.")
                    mg.showinfo("Information","NOTE:\n------\nYour previous tasks might be retrived if you follow this steps\n\n1. Add new task\n2. Add previous tasks above the new task added\n3. Close and re-open the app.\n\nPlease cearfully follow these steps\nfor proper recovery of you tasks ") 

    def delete_all_tasks(self,list_box):
        
        if mg.askyesno("Question","Do you realy want to clear all tasks?"):
            list_box.delete(0,tk.END)
            with open("task_list.txt","w", encoding="UTF-8")  as f:
                pass
            mg.showinfo("Info","Tasks cleared!")

    def load_task(self,list_box):
        # load previous task(s)
        try:
            with open("task_list.txt","r",encoding="UTF-8") as f:
                for  val in f.readlines():
                    if  val == "\n":
                        continue
                    list_box.insert(tk.END,val.strip())
        except:pass

    def on_close(self,root):
        if mg.askyesno("Question","Do you realy want to close the  app?"):
            root.destroy()

    def on_enter(self,list_box):
        self.add_task(self.entry,list_box)

    def change_bg(self,root):
        root.config(bg="lightblue")
            

    def change_bg2(self,root):

        root.config(bg="white")

    def helpnote(self,root):
        new_top = tk.Toplevel(root)
        #newtop.destroy()
        
        new_top.title("Help")
        new_top.geometry("600x500")
        new_top.minsize(500,400)
        new_top.maxsize(700,700)
  
        text_widget= tk.Text(new_top,state=tk.DISABLED)
        text_widget.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
        scroll_bar = tk.Scrollbar(new_top)
        scroll_bar.pack(side=tk.LEFT,fill=tk.BOTH)
        text_widget.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=text_widget.yview)

        # add text
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END,HELP_NOTE)
        text_widget.config(state=tk.DISABLED)
    
        
        

class MenuBar(Base):
    """MenuBar class to build the menu bar options

    Options:
        - Option menu:
        --------------
              - (Close): closes the app
                
        - Settings menu:
        ----------------
              - (Add task without message):  sets ENABLE_ADD_MESSAGE to Flase 
                    if True, not to allow 'Task Added'  popup
              - (Add task with message): sets ENABLE_ADD_MESSAGE to True
                    if False, to allow 'Task Added' popup
                
              - (Disable entry warning): sets ENABLE_EMPTY_MESSAGE to False
                    if True, not to allow 'Task input is empty'  popup
              - (Enable entry warning): sets ENABLE_EMPTY_MESSAGE to True
                    if False, to allow 'Task input is empty' popup

        - Help menu: Shows help"""
    
    def __init__(self,root,list_box):
        # call to super() to use the  'root' attr
        super().__init__(root)

        self.list_box = list_box

        # menu bar
        self.menu_bar = tk.Menu(self.root)
        
        self.option_menu = tk.Menu(self.menu_bar,tearoff=0)
        self.setting_menu = tk.Menu(self.menu_bar,tearoff=0)
        #self.help_menu = tk.Menu(self.menu_bar,tearoff=0)arof
        self.colour_menu = tk.Menu(self.menu_bar,tearoff=0)
        self.help_menu = tk.Menu(self.menu_bar,tearoff=0)
        
        self.menu_bar.add_cascade(label="Option",menu = self.option_menu)
        self.menu_bar.add_cascade(label="Settings",menu = self.setting_menu)
        self.menu_bar.add_cascade(label="Theme",menu = self.colour_menu)
        self.menu_bar.add_cascade(label="Help",menu=self.help_menu )
        

        self.setting_menu.add_command(label="Add task without message",command= lambda: self.enable_add_msg(False))
        self.setting_menu.add_command(label="Add task with message",command= lambda: self.enable_add_msg(True))
        self.setting_menu.add_separator()
        self.setting_menu.add_command(label="Disable entry warning",command= lambda: self.enable_empty_msg(False))
        self.setting_menu.add_command(label="Enable entry warning",command=lambda: self.enable_empty_msg(True))

        self.option_menu.add_command(label="Close without question",command=self.root.destroy)
        self.option_menu.add_separator()
        self.option_menu.add_command(label="Delete all tasks",command=lambda:self.delete_all_tasks(self.list_box))

        self.colour_menu.add_command(label="Light Blue",command=lambda: self.change_bg(root))
        self.colour_menu.add_command(label="White",command=lambda: self.change_bg2(root))

        self.help_menu.add_command(label="Getting started",command= lambda:self.helpnote(root))
        # Add menu bar to root    
        self.root.config(menu=self.menu_bar)

        
    def enable_add_msg(self,bool):
        '''either enable or disable "Task Added" popup'''
        
        global ENABLE_ADD_MESSAGE
        
        if bool == False:
            ENABLE_ADD_MESSAGE = False
        elif bool == True:
            ENABLE_ADD_MESSAGE = True
            
    def enable_empty_msg(self,bool):
        '''either enable or disable "Task Input is empty!" popup'''
        global ENABLE_EMPTY_MESSAGE
        
        if bool == True:
            ENABLE_EMPTY_MESSAGE = True
            
        elif bool == False:
            ENABLE_EMPTY_MESSAGE = False



class ToDoList(Base):
    """ToDoList class

        builds the main interface of the todolist app.
        instanciates MenuBar class to build the  menu bar and uses the base
        class methods and attr

        Args:
        -----
            - root(tkinter window): creates tk window."""
     
    def __init__(self,root):
       
        # call the super() to use the  'root' attr
        super().__init__(root)
        
        self.x = int((root.winfo_screenwidth()-WIDTH)/2)
        self.y = int((root.winfo_screenheight()-HEIGHT)/2)
        
        self.root.title("To Do List")
        self.root.geometry("%dx%d+%d+%d"%(WIDTH,HEIGHT,self.x,self.y))
        self.root.config(bg="white")
        #self.root.minsize(300,700) 
        #self.root.maxsize(WIDTH,805)
        self.root.resizable(False,False)

        # top level
        tk.Label(self.root,text='',bg=BACKGROUND_COLOR,width=WIDTH,height=4).place(x=0,y=0,relwidth=1)
        all_task_label = tk.Label(self.root,text="ALL Task",font="Arial 15 bold",
                                  bg=BACKGROUND_COLOR,fg="white").pack(pady=25)

        # frame for  entry and  add widget (eb_frame)
        self.eb_frame = tk.Frame(self.root)
        
        self.eb_frame.pack_propagate(False)
        self.eb_frame.config(width=WIDTH)
        self.eb_frame.columnconfigure(0,weight=1)
        self.eb_frame.pack(fill=tk.X,pady=200)
        
        self.entry = tk.Entry(self.eb_frame,font="Roboto 15",highlightbackground=BACKGROUND_COLOR,
                              highlightthickness=1,bd=0)
        self.entry.grid(row=0,column=0,sticky=tk.W+tk.E)
        # call the cursor to show when program starts
        self.entry.focus()

        # Add button
        self.add_button = tk.Button(self.eb_frame,text="ADD",width=5,bg="blue",fg="white",
                               bd=0,font="Arial 11 bold")
        self.add_button.grid(row=0,column=1)

        
        ## list box frame
        self.list_box_frame = tk.Frame(self.root)

        self.list_box_frame.pack_propagate(False)
        self.list_box_frame.config(width=WIDTH,height=300)
        self.list_box_frame.place(x=0,y=320,relwidth=1,anchor="nw")  #in_ = root,bordermode="outside",border=10)

        # list box
        self.list_box = tk.Listbox(self.list_box_frame,selectmode=tk.SINGLE,
                                   width=35,bg=BACKGROUND_COLOR,height=300,
                                   fg="white",selectbackground="grey",
                                   font="Arial' 12 bold ",cursor="hand2")

        # instantiate MenuBar and  pass list_box
        menu = MenuBar(root,self.list_box)
        # from the, Base blass Load all task
        self.load_task(self.list_box)
        self.entry.bind("<Return>",lambda event: self.on_enter(self.list_box))
        
        self.list_box.pack(side=tk.LEFT,fill=tk.X,padx=2)

        #scroll bar
        self.scroll_bar =  tk.Scrollbar(self.list_box_frame)
        self.scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
        # connect scroolbar to  list_box
        self.list_box.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.list_box.yview)

    
        #--------------------------------------------------------------
        # add command to add button from the Base class -> super().add_task(parameters)
        self.add_button.config(command= lambda:self.add_task(self.entry,self.list_box))
        #--------------------------------------------------------------
        
        # delete button
        self.delete_button = tk.Button(self.root,text="DELETE",font="Arial 12 bold",fg="red",bg="white",
                                       bd=0,cursor="hand2",command=lambda:self.delete_task(self.list_box))
        self.delete_button.pack(side=tk.BOTTOM)
        

        close = self.root.protocol("WM_DELETE_WINDOW" ,lambda:self.on_close(root))

                
if __name__ == "__main__":
    root  = tk.Tk()
    
    td = ToDoList(root)
        
    root.mainloop()

